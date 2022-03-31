from django.shortcuts import render
from .forms import UserSignupForm

# Create your views here.

def home(request):
    return render(request, "user/home.html", {})



def signup(request):
    form = UserSignupForm
    return render(request, 'user/signup.html', {'form':form})

