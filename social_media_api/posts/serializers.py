from rest_framework import serializers
from .models import Post, Comment, Like

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(read_only=True, source='author')
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "author", "author_id", "title", "content",
                  "created_at", "updated_at", "comments_count"]
        read_only_fields = ["id", "author", "author_id", "created_at", "updated_at", "comments_count"]

    def to_representation(self, instance):
        # Efficiently annotate count if not provided by queryset
        rep = super().to_representation(instance)
        if "comments_count" not in rep or rep["comments_count"] is None:
            rep["comments_count"] = instance.comments.count()
        return rep
        

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        read_only=True, source="author"
    )

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "author_id", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "author", "author_id", "created_at", "updated_at"]


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ["id", "user", "post", "created_at"]
        read_only_fields = ["id", "user", "created_at"]