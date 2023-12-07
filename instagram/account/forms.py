from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


"""a form to sign up a new user"""
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control"
            }),
             "password1": forms.PasswordInput(attrs={
                "class": "form-control"
            }), 
            "password2": forms.PasswordInput(attrs={
                "class": "form-control"
            }),
        }

"""sign in form"""
class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control"
            }),
             "password": forms.PasswordInput(attrs={
                "class": "form-control"
            }), 
        }