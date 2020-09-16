from django.db import models
from users.models import User

 

# Create your models here.

class Album(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    title = models.TextField(max_length=35)
    description = models.TextField(max_length=100,blank=True)
    public = models.BooleanField(default=True, blank=True)
    #default_photo = models.Foreignkey(to="Photo", on_delete=models.CASCADE, blank=True, null=True)
    #created = models.DateTimeField(auto_now_add=True)
    #photos = models.ManyToManyField(to="Photo", on_delete=models.CASCADE)


class Photo(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.TextField(max_length=35)
    image = models.FileField(upload_to="images/")
    description = models.TextField(max_length=100, blank=True)
    #comments = models.ForeignKey(to="Summary", on_delete=models)
    #created = models.DateTimeField(auto_now_add=True, )
    albums = models.ManyToManyField(Album, blank=True)


class Summary(models.Model):
    body = models.TextField(max_length=350)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    #photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    #created = models.DateTimeField(auto_now_add=True)

#class Profile(models.Model):
