from django import forms
from django.http import request

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

    def __init__(self, *args, **kwargs):
        self.logged_in_user = kwargs.pop("logged_in_user", None)
        super(NewPostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super(NewPostForm, self).save(commit=False)
        post.author_id = self.logged_in_user.id
        if commit:
            post.save()
        return post
