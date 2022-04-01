from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# from user import views as user_view

urlpatterns = [
    path('', views.index, name='index'),
    # path("profile/<username>/", user_view.profile_page, name="profile-page"),
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
