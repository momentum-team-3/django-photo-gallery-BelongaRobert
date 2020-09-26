from rest_framework import serializers
from gallery.models import Album, Photo

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = [
            'owner',
            'title',
            'default_photo',
            'public',
        ]

class PhotoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Photo
        fields = [
            "owner",
            "title",
            "created",
            "album",
        ]