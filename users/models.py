from django.db import models

# to extend the User model, we've imported it
from django.contrib.auth.models import User

# Importing from the Pillow library
from PIL import Image

class Profile(models.Model):

    # to have a one to one relationship with the user model
    # CASCADE - If the user is deleted, then also delete the profile, and NOT the other way around.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # default.jpg : the default image
    # profile_pics : the directory to which profile pics will get uploaded to when user uplooads one.
    
    # to use the imagefield, we need to use Pillow
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # to keep our model a bit more descriptive
    def __str__(self):
        return f'{self.user.username} Profile'
    
    # overriding the save method to implement auto resizing of the image while uploading.
    def save(self, *args, **kwargs):
        # running this save method from our parent class first.
        super().save(*args, **kwargs)

        # now we grab the image it saved and we are resizing it.

        # opens the image of the current instance.
        img = Image.open(self.image.path)

        # Large image gets resized to a small image and due to this, a lot of space on
        # server can be saved.
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)    

