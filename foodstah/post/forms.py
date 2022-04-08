from django import forms

from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "post_description",
            "main_image",
            "is_recipe",
            "ingredients",
            "recipe_description",
            "cooking_time",
            ]