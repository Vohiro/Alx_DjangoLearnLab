from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly


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
        serializer.save(author=self.request.user)