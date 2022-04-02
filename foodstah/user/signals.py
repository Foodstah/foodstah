# This is a post save signal that will be triggered when an object is saved.
from django.db.models.signals import post_save

# The user model is sending the signal
from django.contrib.auth.models import User

# The receiver is a signal that receives the signal and performs a task
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    instance.profile.save()
