from django.views.generic import (
    TemplateView, 
    CreateView, 
    ListView, 
    DetailView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, PostForm, CommentForm
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.http import require_POST

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


class HomeView(TemplateView):
    template_name = 'blog/home.html'


class PostsView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        context['comments'] = post.comments.all().order_by('-created_at')
        context['form'] = CommentForm()

        return context


class PostCreatView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

@login_required
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been update successfully!')
            return redirect('home')
        
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'blog/profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
@require_POST
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
        messages.success(request, 'Your comment was added successfully.')
    else:
        messages.error(request, 'There was an error adding your comment.')

    return redirect ('post_detail', pk=post.pk)

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment was update.')
            return redirect ('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Your comment was deleted.')
        return redirect ('post_detail', pk=comment.post.pk)
    
    return render(request, 'blog/delete_comment.html', {'comment': comment})