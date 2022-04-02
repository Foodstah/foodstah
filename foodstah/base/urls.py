from django.urls import path
from . import views

# from user import views as user_view

urlpatterns = [
    path("", views.index, name="index"),
]
