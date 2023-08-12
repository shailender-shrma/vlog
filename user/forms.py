from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Signup(UserCreationForm):
    username = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(max_value=10)
    

    class Meta:
        model = User
        fields = ("username", "email", "phone","password1", "password2")
