#from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, FormView
from django.views.generic.base import RedirectView
#from django.urls import redirect
from django.shortcuts import redirect
#from django.contrib.auth.decorators import login_required
from .forms import AddAlbumForm, AddPhotoForm, AddCommentForm
from gallery.models import Photo, Album
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(TemplateView):
    template_name = "photos/home.html"

class PhotoList(LoginRequiredMixin, ListView):
    model = Photo
    template_name = "photos/photo_list.html"
    photos = Photo.objects.all()

class PhotoView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = "photos/photo_view.html"
    
class AlbumList(LoginRequiredMixin, ListView):
    model = Album
    template_name = "photos/album_list.html"
    queryset = Album.objects.all()
    

class AlbumView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = "photos/album_view.html"
    queryset = Album.objects.all()

   
class DeletePhoto(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = "delete_photo.html"

class AddAlbum(LoginRequiredMixin, FormView):
    form_class = AddAlbumForm
    template_name = "photos/add_album.html"
    fields = ['owner', 'title', 'description', 'public', ]
    queryset = Album.objects.all()
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class AddPhoto(LoginRequiredMixin, FormView):
    form_class = AddPhotoForm
    template_name = "photos/add_photo.html"
    fields = ['owner', 'title', 'image', 'description', 'public']
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

class Login(RedirectView):
    template_name = "auth_login.html"
            
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "auth_login.html"
    


class AddComment(LoginRequiredMixin, FormView):
    form_class = AddCommentForm
    template_name = 'photos/add_comment.html'
    fields = ['body', 'owner', 'photo_of']
    success_url = 'photos/photo_view.html'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)