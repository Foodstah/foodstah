from django.shortcuts import render

# Create your views here.


def post(request):
    context = {}
    return render(request, "post/food-feed.html")
    # if request.user.is_authenticated():
    #     return render(request, 'post/food-feed.html')
    # else:
    #     return render(request, 'user/signup.html')
