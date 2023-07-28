from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class MyRegisterForm(UserCreationForm):
    ''' Create a new user registration form based on Bulit-in one. This form will have email address field additional'''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')