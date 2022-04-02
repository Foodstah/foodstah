from django.urls import path
from . import views

urlpatterns = [
    path("food-feed/", views.post, name="food-feed"),
    path("add-post/", views.add_post, name="add-post"),
]
