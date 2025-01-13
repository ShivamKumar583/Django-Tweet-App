from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet,User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        # ye text photo model ki entity h
        fields = ['text' , 'photo',]

class UserRegistratinoForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2')