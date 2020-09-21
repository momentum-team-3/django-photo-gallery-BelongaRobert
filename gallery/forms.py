from django.forms import ModelForm
from .models import Photo, Album, Summary

class AddAlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = [
            #'owner',
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
            #'owner',
            'title',
            'media',
            'description',
            #'created',
            'albums_in',
            'public',
            
        ]


class AddCommentForm(ModelForm):
    class Meta:
        model = Summary
        fields = [
            'owner',
            'body',
            'photo_of',
            #'created',
        ]