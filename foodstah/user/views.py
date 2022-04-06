from django.contrib.auth.models import User
from django.urls import reverse
from django.views.decorators.http import require_POST

from django.shortcuts import render, redirect

from .models import Profile, Following
from .forms import UserSignupForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView

# Create your views here.


def home(request):
    if request.user.is_authenticated():
        return render(request, "post/food-feed.html", {})
    else:
        return render(request, "base/index.html")


def login(request):
    return render(request, "user/login.html")


class Logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)


def signup(request):

    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account successfully created for {username}!")
            return redirect("login")

    else:
        form = UserSignupForm()

    return render(request, "user/signup.html", {"form": form})


def profile_page(request, username):
    profile = User.objects.get(username=username)
    profile_followers = len(Following.objects.filter(user=profile))
    profile_following = len(Following.objects.filter(follower=profile))

    # the logic for whether logged in profile is already following or not
    # -> whether to display follow or unfollow
    followlist1 = Following.objects.filter(user=profile)
    followlist2 = []
    follow_button_value = ""
    for follower in followlist1:
        followlist1 = follower.follower
        followlist2.append(followlist1)
        if profile in followlist2:
            follow_button_value = "unfollow"
        else:
            follow_button_value = "follow"

    # the context
    context = {
        "profile": profile,
        "profile_followers": profile_followers,
        "profile_following": profile_following,
        "follow_button_value": follow_button_value,
    }

    return render(request, "user/profile_page.html", context)


# all the functions for following are below

@require_POST
def followers_count(request):
    value = request.POST["value"]
    user = request.POST["user"]
    follower = request.POST["follower"]
    if value == "follow":
        followers_cnt = Following.objects.create(follower=follower, user=user)
        followers_cnt.save()
    if value == "unfollow":
        followers_cnt = Following.objects.get(follower=follower, user=user)
        followers_cnt.delete()
    return redirect("profile-page", username=user)
