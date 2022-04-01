from django.urls import path
from . import views

urlpatterns = [
    path("food-feed/", views.post, name="food-feed"),
]
