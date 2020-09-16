from django.db import models
from users.models import User
 

# Create your models here.

class Album(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=35)
    description = models.TextField(max_length=100,blank=True)
    public = models.BooleanField(default=False)

class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=35)
    image = models.FileField(upload_to="images/")
    comments = models.TextField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    albums = models.ManyToManyField(Album, blank=True)

class Comment(models.Model):
    body = models.TextField(max_length=350)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)