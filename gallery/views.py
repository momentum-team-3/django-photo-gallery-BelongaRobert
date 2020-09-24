#from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, FormView, UpdateView
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.shortcuts import redirect
#from django.contrib.auth.decorators import login_required
from .forms import AddAlbumForm, AddPhotoForm, AddCommentForm
from gallery.models import Photo, Album, Comment
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(TemplateView):
    template_name = "photos/home.html"

class PhotoList(LoginRequiredMixin, ListView):
    model = Photo
    template_name = "photos/photo_list.html"
    def get_queryset(self):
        return self.request.user.albums.photos.all()
    


class CommentListView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = "photos/view_comment.html"
    def get_queryset(self):
        return self.request.photo.summaries.all()

    def get_context_data(self, **kwargs):
        context = super(CommentListView, self).get_context_data(**kwargs)
        summaries = self.get_queryset()
        context['summaries'] = summaries
        return context


class AlbumList(LoginRequiredMixin, ListView):
    model = Album
    template_name = "photos/album_list.html"
    def get_queryset(self):
        return self.request.user.albums.all()

    def get_context_data(self, **kwargs):
        context = super(AlbumList, self).get_context_data(**kwargs)
        albums = self.get_queryset()
        #cover_photo = self.request.GET.get('default_photo')
        context['albums'] = albums
        return context


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

            
class EditAlbum(LoginRequiredMixin, UpdateView):
    model = Album
    fields = ['owner','title', 'description', 'public']
    template_name = "photos/edit_album.html"
    success_url = reverse_lazy('album_list')
    def get_success_url (self):
        return f"/albums/view/{self.kwargs['pk']}"

class AddPhoto(LoginRequiredMixin, FormView):
    form_class = AddPhotoForm
    template_name = "photos/add_photo.html"
    fields = ['owner', 'title', 'image', 'description', 'public']
    queryset = Photo.objects.all()
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
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)