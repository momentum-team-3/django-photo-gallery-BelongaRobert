from django.forms import ModelForm
from .models import Photo, Album, Comment

class AddAlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'description',
            'public',
            #'created',
            'default_photo',
        ]



class AddPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = [
            'title',
            'media',
            'description',
            #'created',
            'albums',
            'public',
            
        ]


class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body',
            #'created',
        ]