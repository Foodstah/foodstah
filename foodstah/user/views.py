from django.contrib.auth.models import User
from django.urls import reverse
from django.views.decorators.http import require_POST

from django.shortcuts import render, redirect
from .models import Profile, Following
from post.models import Post
from .forms import UserSignupForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView

# Create your views here.


def home(request):
    if request.user.is_authenticated():
        return render(request, "post/food-feed.html", {})
    else:
        return render(request, "base/index.html")


class Login(LoginView):
    """ Must enter a login view with login username as lower() """
    pass


class Logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You have successfully logged out.")
        return super().dispatch(request, *args, **kwargs)


def signup(request):

    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            print("SAVE")
            form.save()
            messages.success(request, f"Account successfully created for {username}!")
            return redirect("login")

    else:
        form = UserSignupForm()

    return render(request, "user/signup.html", {"form": form})


def profile_page(request, username):
    profile = User.objects.get(username=username)

    profile_posts = len(Post.objects.filter(author=profile))

    profile_followers = len(Following.objects.filter(user=profile))
    profile_following = len(Following.objects.filter(follower=profile))

    # the logic for whether logged in profile is already following or not
    # -> whether to display follow or unfollow
    followlist1 = Following.objects.filter(user=profile)
    followlist2 = []
    follow_button_value = "follow"
    for follower in followlist1:
        followlist1 = follower.follower
        followlist2.append(followlist1)
        if profile in followlist2:
            follow_button_value = "unfollow"
        else:
            follow_button_value = "follow"

    
    user_posts = Post.objects.filter(author=profile)




    # the context
    context = {
        "profile": profile,
        "profile_followers": profile_followers,
        "profile_following": profile_following,
        "follow_button_value": follow_button_value,
        "profile_posts": profile_posts,
        "user_posts": user_posts
    }
    return render(request, "user/profile_page.html", context)


# all the functions for following are below


def update_profile(request, username):
    # update profile form
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, files=request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account details have been updated.')
            return redirect("profile-page", username=username)
    form = ProfileForm(instance=request.user.profile)
    return render(request, "user/update_profile_page.html", {"form": form})


@require_POST
def followers_count(request):
    value = request.POST["value"]
    # what fixed this?:
    # First, get the raw usernames of both the user and follower from the page
    # Load the related object from the model
    # Then we will create / delete the object from the Follower
    user = User.objects.get(username=request.POST["user"])
    follower = User.objects.get(username=request.POST["follower"])
    if value == "follow":
        followers_cnt = Following.objects.create(follower=follower, user=user)
        followers_cnt.save()
        print(follower, user)
    if value == "unfollow":
        followers_cnt = Following.objects.get(follower=follower, user=user)
        followers_cnt.delete()
    return redirect("profile-page", username=user)
