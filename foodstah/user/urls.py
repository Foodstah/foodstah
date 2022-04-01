from django.urls import path
from  user import views as user_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("", user_view.home, name="home"),
    path("profile/<username>/", user_view.profile_page, name="profile-page"),
    path("signup/", user_view.signup, name="signup"),
    path("login/", auth_view.LoginView.as_view(template_name='user/login.html'), name="login"),
    path("logout/", user_view.Logout.as_view(template_name='user/logout.html'), name="logout"),
    path("profile/<int:id>/", user_view.profile_page, name="profile-page")
]
