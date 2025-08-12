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
    PostDeleteView
    )


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('posts', PostsView.as_view(), name='posts'),
    path('profile/', profile_view, name='profile'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='Post_detail'),
    path('posts/new/', PostCreatView.as_view(), name='post_new'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]