from django.shortcuts import get_object_or_404, render, redirect
from .forms import NewPostForm
from .models import Post
from django.contrib import messages

# Create your views here.

def post(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request, 'post/food-feed.html', {'posts':posts})

def add_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, "Your post was added successfully.")
            return redirect("food-feed")

        messages.error(request, "Unsuccessful. Could not add new post.")

    form = NewPostForm()
    return render(request, "post/add_post.html", {"addpost_form": form})

def give_like(request,pk):
    post = get_object_or_404(Post,id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user.id)
    return redirect("/food-feed")

def give_love(request,pk):
    post = get_object_or_404(Post,id=pk)
    if request.user in post.loves.all():
        post.loves.remove(request.user)
    else:
        post.loves.add(request.user.id)
    return redirect("/food-feed")

def give_drooling_face(request,pk):
    post = get_object_or_404(Post,id=pk)
    if request.user in post.drooling_faces.all():
        post.drooling_faces.remove(request.user)
    else:
        post.drooling_faces.add(request.user.id)
    return redirect("/food-feed")