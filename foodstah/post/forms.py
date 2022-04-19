from django import forms

from .models import Post, Comment


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

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "body"
        ]
