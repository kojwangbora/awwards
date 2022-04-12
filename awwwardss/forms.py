from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, Rating


# from pyuploadcare.dj.forms import ImageField

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=40, help_text='Required. Inform a valid email adress.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    photo = forms.ImageField(label='')

    class Meta:
        model = Post
        fields = ('photo', 'title', 'url', 'description', 'technologies',)