from django.contrib import admin
from gallery.models import Album, Photo, Summary

# Register your models here.
admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Summary)