from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import NewPostForm
from .models import Post


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

        messages.info(request, "If you're adding a recipe you must include the ingredients, instructions and cooking time.")

    form = NewPostForm()
    return render(request, "post/add_post.html", {"addpost_form": form})

def give_like(request,pk):
    post = get_object_or_404(Post,id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user.id)
    if request.META['HTTP_ACCEPT'] == "application/json":
        return JsonResponse({"reactions": post.likes.count()})
    return redirect("/food-feed")

def give_love(request,pk):
    post = get_object_or_404(Post,id=pk)
    if request.user in post.loves.all():
        post.loves.remove(request.user)
    else:
        post.loves.add(request.user.id)
    if request.META['HTTP_ACCEPT'] == "application/json":
        return JsonResponse({"reactions": post.loves.count()})
    return redirect("/food-feed")

def give_drooling_face(request,pk):
    post = get_object_or_404(Post,id=pk)
    if request.user in post.drooling_faces.all():
        post.drooling_faces.remove(request.user)
    else:
        post.drooling_faces.add(request.user.id)
    if request.META['HTTP_ACCEPT'] == "application/json":
        return JsonResponse({"reactions": post.drooling_faces.count()})
    return redirect("/food-feed")

class PostDetailsView(DetailView):
    model = Post
    context_object_name = 'post'

class PostUpdateView(UpdateView):
    model = Post
    fields = [
            "title",
            "post_description",
            "main_image",
            "is_recipe",
            "ingredients",
            "recipe_description",
            "cooking_time",
            ]
    template_name = 'post/post-update.html'
    context_object_name = 'post'

class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('food-feed')