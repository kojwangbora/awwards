from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=40, help_text='Required. Inform a valid email adress.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')