from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    topic = models.CharField(max_length=200, blank= True)
    content = models.TextField()
    date_of_post = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})   