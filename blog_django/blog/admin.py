from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'published_date')
    list_filter = ['published_date']
    search_fields = ['title', 'author']

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at')
    list_filter = ['created_at']
    search_fields = ['author']

admin.site.register(Comment, CommentAdmin)
