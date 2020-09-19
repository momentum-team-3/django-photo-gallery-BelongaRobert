
from django.db import models
from users.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

 

# Create your models here.

class Album(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="albums")
    title = models.TextField(max_length=35)
    description = models.TextField(max_length=100, blank=True)
    public = models.BooleanField(default=True)
    #default_photo = models.ForeignKey(to="Photo", on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    photos = models.ManyToManyField(to="Photo", related_name="albums")

    def __str__(self):
        return f'{self.title}'

class Photo(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=False)
    title = models.TextField(max_length=35)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    image_medium = ImageSpecField(source="images/", processors=[ResizeToFit(200,200)], format='jpeg', options={'quality':100} )
    image_thumb = ImageSpecField(source="images/", processors=[ResizeToFill(200,200)],format='jpeg', options={'quality':100})
    description = models.TextField(max_length=100, blank=True)
    comments = models.ForeignKey(to="Summary", on_delete=models.CASCADE, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    albums_in = models.ForeignKey(to="Album", on_delete=models.CASCADE, blank=False, null=False, related_name="Album")


class Summary(models.Model):
    body = models.TextField(max_length=350)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=False, null=False )
    photo_of = models.ForeignKey(to="Photo", on_delete=models.CASCADE, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
