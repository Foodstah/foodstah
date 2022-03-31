from django.shortcuts import render

from .models import Profile
from .forms import UserSignupForm

# Create your views here.

def home(request):
    return render(request, "user/home.html", {})


def signup(request):
    form = UserSignupForm
    return render(request, 'user/signup.html', {'form':form})

def profile_page(request, id=1):
    profile = Profile.objects.get(id=id)
    return render(request, "user/profile_page.html", {"profile": profile})
