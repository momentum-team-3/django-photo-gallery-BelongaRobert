from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView
from gallery.models import Photo, Album
# Create your views here.

class HomeView(TemplateView):
    template_name = "photos/home.html"

class PhotoList(ListView):
    model = Photo
    template_name = "photos/photo_list.html"
    photos = Photo.objects

class PhotoView(DetailView):
    model = Photo
    template_name = "photos/photo_view.html"
    
class AlbumList(ListView):
    model = Album
    template_name = "photos/album_list.html"
    
class AlbumView(DetailView):
    model = Album
    template_name = "photos/album_view.html"
    
class DeletePhoto(DeleteView):
    model = Photo
    template_name = "delete_photo.html"

class AddPhoto(CreateView):
    model = Photo
    template_name = "add_photo.html"
    