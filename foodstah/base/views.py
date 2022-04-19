from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, "base/index.html")

def investor_relations(request):
    return render(request, "base/investor-relations.html")
