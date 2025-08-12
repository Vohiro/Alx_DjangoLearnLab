from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comment

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pics']

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text='Comma-separated tags')

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
