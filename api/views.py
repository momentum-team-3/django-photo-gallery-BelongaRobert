from rest_framework import generics
from api.serializers import AlbumSerializer, PhotoSerializer
from gallery.models import Album, Photo


class AlbumListView(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return self.request.user.albums

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class PhotoListView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
