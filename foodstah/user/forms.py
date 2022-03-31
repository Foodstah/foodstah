from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import re

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def clean_username(self):
            username = self.cleaned_data['username']
    
            if not re.match(r'^[A-Za-z0-9_-]+$', username):
                raise forms.ValidationError("Sorry , you can only have alphanumeric, _ or - in username")