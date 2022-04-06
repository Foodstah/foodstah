from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    description = models.TextField(default=None, max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, default="")

    # posts =
    # following =
    # followers =

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Following(models.Model):
    follower = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    def __str__(self):
        return self.user


    # user_id = models.ForeignKey(Profile, related_name="following", on_delete=models.CASCADE)

    # following_user_id = models.ForeignKey(Profile, related_name="followers", on_delete=models.CASCADE)
