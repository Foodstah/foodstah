from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import NewPostForm

# Create your views here.

def post(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request, 'post/food-feed.html', {'posts':posts})


def add_post(request):
    form = NewPostForm()

    if request.method == 'POST':
       form = NewPostForm(request.POST, request.FILES)

       if form.is_valid():
           form.save()
           return HttpResponseRedirect('food-feed')

    return render(request,'post/add_post.html', {'form':form})
    