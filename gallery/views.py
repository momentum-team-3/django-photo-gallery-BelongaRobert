#from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.base import RedirectView
from django.shortcuts import redirect
#from django.contrib.auth.decorators import login_required
from .forms import AddAlbumForm, AddPhotoForm, AddCommentForm
from gallery.models import Photo, Comment, Album
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render

# Create your views here.

class HomeView(ListView):
    template_name = "photos/home.html"
    model = Photo
    queryset = Photo.objects.all()

class PhotoList(View):
    def get(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        return render(request, "photos/photo_list.html", {"album": album})
    

class CommentListView(View):
    def get(self, request, pk):
        photo = get_object_or_404(Photo, pk=pk)
        return render(request, 'photos/view_comment.html', {"photo": photo})

class list_all_albums(ListView):
    model = Album
    template_name = 'photos/list_all_albums.html'
    queryset = Album.objects.all()


class AlbumList(LoginRequiredMixin, ListView):
    model = Album
    template_name = "photos/album_list.html"
    def get_queryset(self):
        return self.request.user.albums.all()

    def get_context_data(self, **kwargs):
        context = super(AlbumList, self).get_context_data(**kwargs)
        albums = self.get_queryset()
        context['albums'] = albums
        return context

class UserPhotos(LoginRequiredMixin, ListView):
    model = Photo
    template_name = "photos/user_photos.html"
    def get_queryset(self):
        return self.request.user.photos.all()

    def get_context_data(self, **kwargs):
        context = super(UserPhotos, self).get_context_data(**kwargs)
        photos = self.get_queryset()
        context['photos'] = photos
        return context

class AlbumView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = "photos/album_view.html"
    queryset = Album.objects.all()

   
class DeletePhoto(LoginRequiredMixin, View):
    def get(self, request, pk):
        photo = get_object_or_404(Photo, pk=pk)
        photo.delete()
        return render(request, "photos/photo_list.html", {"photo": photo})
   

class AddAlbum(LoginRequiredMixin, FormView):
    form_class = AddAlbumForm
    template_name = "photos/add_album.html"
    fields = ['owner', 'title', 'description', 'public', ]
    queryset = Album.objects.all()
    success_url = 'list_all_albums'
    
    def form_valid(self, form):
        album = form.save(commit=False)
        album.owner = self.request.user
        album.save() 
        return redirect(self.success_url)

class EditAlbum(LoginRequiredMixin, View):
    def get(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        return redirect(request, "photos/list_all_albums.html", {"album": album})
                 

class AddPhoto(LoginRequiredMixin, FormView):
    form_class = AddPhotoForm
    template_name = "photos/add_photo.html"
    fields = ['owner', 'title', 'image', 'description', 'public']
    queryset = Photo.objects.all()
    success_url = 'view_comment'
    
    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.owner = self.request.user
        photo.save()
        return redirect(self.success_url, pk=photo.pk)

class Login(RedirectView):
    template_name = "auth_login.html"
            
class ProfileView(LoginRequiredMixin, View):
    model = User
    template_name = "profile.html"
    

class AddComment(LoginRequiredMixin, FormView):
    form_class = AddCommentForm
    template_name = 'photos/add_comment.html'
    fields = ['body', 'owner', 'photo_of']
    success_url = 'view_comment'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.owner = self.request.user
        comment.save() 
        return redirect(self.success_url)