from django.db import models
from users.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

 

# Create your models here.

class Album(models.Model):
    #owner = models.ForeignKey(to="User", on_delete=models.CASCADE, blank=False)
    title = models.TextField(max_length=35)
    description = models.TextField(max_length=100,blank=True)
    public = models.BooleanField(default=True, blank=True)
    #default_photo = models.ForeignKey(to="Photo", on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    photos = models.ManyToManyField(to="Photo")


class Photo(models.Model):
    #owner = models.ForeignKey(to="User", on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=35)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField(max_length=100, blank=True)
    #comments = models.ForeignKey(to="Summary", on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True )
    albums = models.ManyToManyField(to="Album", blank=True)


class Summary(models.Model):
    body = models.TextField(max_length=350)
    #owner = models.ForeignKey(to="User", on_delete=models.CASCADE, )
    #photo = models.ForeignKey(to="Photo", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

#class Profile(models.Model):
