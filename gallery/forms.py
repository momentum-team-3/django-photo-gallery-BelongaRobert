from django.forms import ModelForm
from .models import Photo, Album

class AddAlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = [
            'owner',
            'title',
            'description',
            'public',
            'created',
        ]


class AddPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = [
            'owner',
            'title',
            'image',
            'description',
            'created',
            'albums',
            
        ]