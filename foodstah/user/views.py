from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserSignupForm

# Create your views here.

def home(request):
    return render(request, "user/home.html", {})


def signup(request):
    form = UserSignupForm
    return render(request, 'user/signup.html', {'form':form})

def profile_page(request, username):
    profile = User.objects.get(username=username)
    return render(request, "user/profile_page.html", {"profile": profile})
