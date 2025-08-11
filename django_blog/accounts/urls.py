from django.urls import path
from django.views.generic import TemplateView
from .views import ProfileView, SignUpView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path("register/", SignUpView.as_view(), name="register"),
]