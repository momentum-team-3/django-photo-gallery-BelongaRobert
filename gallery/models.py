
from django.db import models
from users.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

 

# Create your models here.

class Album(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name="albums")
    title = models.TextField(max_length=150)
    description = models.TextField(max_length=300, blank=True)
    public = models.BooleanField(default=True)
    default_photo = models.ForeignKey(to="Photo", on_delete=models.DO_NOTHING, blank=True, null=True, related_name='default_photo')
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.title}'

class Photo(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='photos')
    title = models.TextField(max_length=150)
    media = models.ImageField(upload_to="media", null=True, blank=True)
    image_medium = ImageSpecField(source="media", processors=[ResizeToFit(300,300)], format='jpeg', options={'quality':80} )
    image_thumb = ImageSpecField(source="media", processors=[ResizeToFill(200,200)],format='jpeg', options={'quality':80})
    description = models.TextField(max_length=500, blank=True)
    #comments = models.ForeignKey(to="comment", on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    public = models.BooleanField(default=True)
    albums = models.ManyToManyField(to=Album, related_name='photos')
    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    body = models.TextField(max_length=1500)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='comments' )
    photo_of = models.ForeignKey(to="Photo", on_delete=models.CASCADE, null=True, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.owner}'