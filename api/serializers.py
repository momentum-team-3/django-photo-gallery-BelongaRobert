from rest_framework import serializers
from gallery.models import Album, Photo, Comment

class AlbumSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Album
        fields = [
            'id',
            'owner',
            'title',
            'description',
            'default_photo',
            'public',
        ]

class PhotoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Photo
        fields = [
            "id",
            "title",
            "description",
            "created",
            "username",
        ]


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "comment",
            "created",
            "username",
        ]       