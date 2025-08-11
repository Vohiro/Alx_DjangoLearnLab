from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Post

class ProfileView(TemplateView):
    template_name = 'blog/profile.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "blog/register.html"

class HomeView(TemplateView):
    template_name = 'blog/home.html'

class PostsView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'

