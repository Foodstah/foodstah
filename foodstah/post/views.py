from django.shortcuts import render, redirect
from .forms import NewPostForm
from .models import Post
from django.contrib import messages

# Create your views here.

def post(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request, 'post/food-feed.html', {'posts':posts})

def add_post(request):

    if request.method == "POST":
        form = NewPostForm(request.POST, logged_in_user=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Your post was successfully added.")
            return redirect("/food-feed")

        messages.error(request, "Unsuccessful. Could not add new post.")

    form = NewPostForm()
    return render(request, "post/add_post.html", {"addpost_form": form})