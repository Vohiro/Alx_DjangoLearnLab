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
    CommentDeleteView,
    PostByTagListView,
    PostBySearchView
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
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('post/comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    path('post/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_list_by_tag'),
    path('search/', PostBySearchView.as_view(), name='posts_by_search'),
]