from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    RegisterView, 
    HomeView, 
    PostsView, 
    profile_view,
    PostDetailView,
    PostCreatView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
    )


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('posts', PostsView.as_view(), name='posts'),
    path('profile/', profile_view, name='profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreatView.as_view(), name='post_new'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('/posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('c/posts/<int:post_id>/comment/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('/posts/<int:post_id>/comment/new/', CommentDeleteView.as_view(), name='delete_comment'),
]