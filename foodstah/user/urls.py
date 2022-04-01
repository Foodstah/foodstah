from django.urls import path
from  user import views as user_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", user_view.home, name="home"),
    path("signup/", user_view.signup, name="signup"),
    path("login/", auth_view.LoginView.as_view(template_name='user/login.html'), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name='user/logout.html'), name="logout"),
    path("profile/<int:id>/", user_view.profile_page, name="profile_page")
]
