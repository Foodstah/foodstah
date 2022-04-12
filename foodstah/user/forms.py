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
                "Sorry, your username must only contain letters, numbers and underscores."
            )

        elif (
            User.objects.exclude(pk=self.instance.pk).filter(username=username).exists()
        ):
            raise forms.ValidationError(f"Username {username} is already in use.")
        else:
            return username

class UserSignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
   
    def clean_username(self):
        username = self.cleaned_data["username"].lower()
        return username


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "image", "description", "website"]
