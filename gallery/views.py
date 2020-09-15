from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
class PhotoList(ListView):
    pass

class PhotoView(DetailView):
    pass

class AlbumList(ListView):
    pass

class AlbumView(DetailView):
    pass