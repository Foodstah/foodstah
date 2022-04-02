from django.shortcuts import render, redirect
from .forms import NewPostForm
from django.contrib import messages

# Create your views here.


def post(request):
    context = {}
    return render(request, "post/food-feed.html")
    # if request.user.is_authenticated():
    #     return render(request, 'post/food-feed.html')
    # else:
    #     return render(request, 'user/signup.html')

def add_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST, logged_in_user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your post was successfully added.")
            return redirect("/")
        messages.error(request, "Unsuccessful. Could not add new post.")
    form = NewPostForm()
    return render(
        request=request,
        template_name="post/add_post.html",
        context={"addpost_form": form},
    )