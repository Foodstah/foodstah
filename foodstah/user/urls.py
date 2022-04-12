from django.urls import path
from user import views as user_view
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", user_view.home, name="home"),
    path("signup/", user_view.signup, name="signup"),
    path(
        "login/",
        user_view.Login.as_view(template_name="user/login.html"),
        name="login",
    ),
    path(
        "logout/",
        user_view.Logout.as_view(template_name="user/logout.html"),
        name="logout",
    ),
    path(
        "password-reset/",
        auth_view.PasswordResetView.as_view(template_name="user/password_reset.html"),
        name="password-reset",
    ),
    path(
        "password-reset/done/",
        auth_view.PasswordResetDoneView.as_view(
            template_name="user/password_reset_done.html"
        ),
        name="password-reset-done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        auth_view.PasswordResetConfirmView.as_view(
            template_name="user/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "profile/<username>/",
        user_view.profile_page,
        name="profile-page",
    ),
    path(
        "followers_count",
        user_view.followers_count,
        name="followers_count",
    ),
    path("profile/<username>/update", user_view.update_profile, name="profile-update"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
