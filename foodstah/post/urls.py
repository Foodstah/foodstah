from django.urls import path
from . import views

urlpatterns = [
    path("food-feed/", views.post, name="food-feed"),
    path("add-post/", views.add_post, name="add-post"),
    path("likes/<int:pk>", views.give_like, name="give-like"),
    path("loves/<int:pk>", views.give_love, name="give-love"),
    path("droolingface/<int:pk>", views.give_drooling_face, name="give-drooling-face")
]
