from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # redirect : will simply redirect us to a specific route &
    # reverse : will return full URL to that route, simply as a string, and the view 
    #           handles the redirect for us.

    # basically django is getting the url to the specific instance of a post.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    

