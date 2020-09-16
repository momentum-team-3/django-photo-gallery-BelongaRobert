from django.db import models
from users.models import User
 

# Create your models here.

class Album(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.TextField(max_length=35)
    description = models.TextField(max_length=100,blank=True)
    public = models.BooleanField(default=False)
    default_photo = models.ImageField
    created = models.DateTimeField(auto_now_add=True)
    photos = models.ManyToManyField(Photo, on_delete=models.CASCADE)


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.TextField(max_length=35)
    image = models.FileField(upload_to="images/")
    description = models.TextField(max_length=50, blank=True)
    comments = models.ForeignKey(Summary, on_delete=models)
    created = models.DateTimeField(auto_now_add=True)
    albums = models.ManyToManyField(Album, blank=True)


class Summary(models.Model):
    body = models.TextField(max_length=350)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)