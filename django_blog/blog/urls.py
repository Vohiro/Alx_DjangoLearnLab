from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileView, RegisterView, HomeView, PostsView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('posts', PostsView.as_view(), name='posts'),
]