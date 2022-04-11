from django.urls import path
from . import views

urlpatterns = [
    path("food-feed/", views.post, name="food-feed"),
    path("add-post/", views.add_post, name="add-post"),
    path("likes/<int:pk>/", views.give_like, name="give-like"),
    path("loves/<int:pk>/", views.give_love, name="give-love"),
    path("droolingface/<int:pk>/", views.give_drooling_face, name="give-drooling-face"),
    
    path("post/<slug:slug>/", views.PostDetailsView.as_view(), name="post-detail"),


    path("post/<int:pk>/update", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete", views.PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/download-recipe", views.recipe_to_pdf, name="download-recipe"),
    path("post/<int:pk>/save", views.save_post, name="save-post"),
    path("post/saved/", views.saved_post, name="saved-posts")
]
