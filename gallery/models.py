from django.db import models
 

# Create your models here.

class Album(models.Model):
    title = models.TextField(max_length=35)
    public = models.BooleanField(default=False)

class Photo(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=35)
    image = models.FileField(upload_to="images/")
    summary = models.TextField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    albums = models.ManyToManyField(Album, blank=True)