from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from taggit.forms import TagWidget

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
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'image']
        widgets = {
            'title': forms.TextInput(),
            'body': forms.Textarea(),
            'tags': TagWidget(), 
            'image': forms.ClearableFileInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']