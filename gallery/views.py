from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from gallery.models import Photo, Album
# Create your views here.

class HomeView(TemplateView):
    template_name = "photos/base.html"

class PhotoList(ListView):
    model = Photo
    template_name = "photos/photo_list.html"

class PhotoView(DetailView):
    model = Photo
    template_name = "photos/photo_view.html"
    
class AlbumList(ListView):
    model = Album
    template_name = "photos/album_list.html"
    

class AlbumView(DetailView):
    model = Album
    template_name = "photos/album_view.html"
    