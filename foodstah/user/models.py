from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.TextField(default=None, max_length=255)
    website = models.URLField(max_length=255, blank=True, null=True)

    # posts =
    # following =
    # followers =


    def __str__(self):
        return f"{self.user.username}'s Profile"