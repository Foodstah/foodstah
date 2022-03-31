from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("profile/<int:id>/", views.profile_page, name="profile_page")
]
