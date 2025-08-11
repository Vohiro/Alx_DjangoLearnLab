from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, HomeView, PostsView, profile_view


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('posts', PostsView.as_view(), name='posts'),
    path('profile/', profile_view, name='profile'),
]