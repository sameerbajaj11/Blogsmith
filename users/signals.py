# Why signals are being used ?
# We're using signals as, whenever we are creating a new user, instead of adding the profile 
# picture manually creating the profile manually, we're autmating it through signals.

# This is a signal that gets fired, after an object is saved.
from django.db.models.signals import post_save

# User is the sender here, he's sending the signal
from django.contrib.auth.models import User

# importing the receiver
from django.dispatch import receiver

# importing Profile from our model, since we'll be creating profile in our function
from .models import Profile

# When a user is saved, then send this signal. Signal is received by this receiver.
# Here, our receiver is this create_profile function.
# This create_profile function runs everytime a new user is created.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    # if user was created, then create the profile with user as its instance.
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    instance.profile.save()
