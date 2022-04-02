from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def index(request):

    return render(request, "base/index.html")


# def get_current_user(request):
#     current_user = request.user
#     context = {
#         "current_user": current_user,
#     }
#     return render(request, 'base/base.html', context)
