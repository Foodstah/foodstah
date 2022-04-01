from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("profile/<username>/", views.profile_page, name="profile-page")
    path("login/", views.login, name="login"),
]
