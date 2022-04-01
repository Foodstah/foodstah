from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from .models import Profile
from .forms import UserSignupForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView

# Create your views here.

def home(request):
    if request.user.is_authenticated():
        return render(request, "post/food-feed.html", {})
    else:
        return render(request, 'base/index.html')

def login(request):
    return render(request, 'user/login.html')

class Logout(LogoutView): 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)

def signup(request):

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}!')
            return(redirect('login'))

    else:
        form = UserSignupForm()

    return render(request, 'user/signup.html', {'form':form})

def profile_page(request, username):
    profile = User.objects.get(username=username)
    return render(request, "user/profile_page.html", {"profile": profile})
