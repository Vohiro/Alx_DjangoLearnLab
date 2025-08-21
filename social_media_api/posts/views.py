from rest_framework import viewsets, generics, permissions, status
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like
from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from notifications.models import Notification
from rest_framework.views import APIView


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filterset_fields = ["author"]            # ?author=<user_id>
    search_fields = ["title", "content"]     # ?search=keyword
    ordering_fields = ["created_at", "updated_at", "title"]  # ?ordering=-created_at

    def get_queryset(self):
        return Post.objects.all().select_related("author").annotate(
            comments_count=Count("comments")
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        # ensure author can't be changed
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["get"])
    def comments(self, request, pk=None):
        """
        Optional convenience sub-route: /posts/<id>/comments/
        """
        post = self.get_object()
        qs = post.comments.select_related("author").all()
        page = self.paginate_queryset(qs)
        ser = CommentSerializer(page or qs, many=True)
        if page is not None:
            return self.get_paginated_response(ser.data)
        return Response(ser.data)
    

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filterset_fields = ["post", "author"]    # ?post=<post_id>
    search_fields = ["content"]              # ?search=keyword
    ordering_fields = ["created_at", "updated_at"]

    def get_queryset(self):
        qs = Comment.objects.all().select_related("post", "author")
        post_id = self.request.query_params.get("post")
        if post_id:
            qs = qs.filter(post_id=post_id)
        return qs

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)

        # Create notification for the post author
        post = comment.post
        if post.author != self.request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=self.request.user,
                verb="commented on",
                target=post
            )


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the users that the current user follows
        following_users = self.request.user.following.all()
        # Get posts by those users
        return Post.objects.filter(author__in=following_users).order_by("-created_at")


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target=post
            )

        return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"detail": "Unliked successfully."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)