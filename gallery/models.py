
from django.db import models
from users.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

 

# Create your models here.

class Album(models.Model):
    owner = models.ForeignKey(to=User, related_name="albums", on_delete=models.CASCADE, blank=False, null=True)
    title = models.TextField(max_length=35)
    description = models.TextField(max_length=100,blank=True)
    public = models.BooleanField(default=True, blank=True)
    default_photo = models.ImageField(upload_to="images/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    #photos = models.ManyToManyField(to="Photo")


class Photo(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=True)
    title = models.TextField(max_length=35)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    image_medium = ImageSpecField(source="images/", processors=[ResizeToFit(200,200)], format='jpeg', options={'quality':100} )
    image_thumb = ImageSpecField(source="images/", processors=[ResizeToFill(200,200)],format='jpeg', options={'quality':100})
    description = models.TextField(max_length=100, blank=True)
    comments = models.ForeignKey(to="Summary", on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True )
    albums = models.ForeignKey(to="Album", on_delete=models.CASCADE, blank=False, null=True)


class Summary(models.Model):
    body = models.TextField(max_length=350)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=True )
    photo_of = models.ForeignKey(to="Photo", on_delete=models.CASCADE, blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=False)
