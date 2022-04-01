
from django.shortcuts import render, redirect
from .models import Profile
from .forms import UserSignupForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "user/home.html", {})

def login(request):
    return render(request, 'user/login.html')


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

def profile_page(request, id=1):
    profile = Profile.objects.get(id=id)
    return render(request, "user/profile_page.html", {"profile": profile})
