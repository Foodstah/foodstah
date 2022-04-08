import imp
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  

from .models import Profile

import re


class UserSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data["username"].lower()

        if not re.match(r"^[A-Za-z0-9_]+$", username):
            raise forms.ValidationError(
                "Sorry , you can only have alphanumeric, _ or - in username"
            )
        else:
            return username

class MyAuthenticationForm(AuthenticationForm):

    def clean_username(self):
        return self.cleaned_data['username'].lower()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "image",
            "description",
            "website"
        ]