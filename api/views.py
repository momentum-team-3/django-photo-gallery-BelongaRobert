from rest_framework import generics, status
from rest_framework.parsers import FileUploadParser, ParseError
from rest_framework.views import Response, APIView
from api.serializers import AlbumSerializer, PhotoSerializer
from gallery.models import Album, Photo
from django.shortcuts import get_object_or_404



class AlbumListView(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return self.request.user.albums

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    def get_queryset(self):
        return self.request.user.albums

class PhotoImageApiView(APIView):
    parser_classes = (FileUploadParser, ) #need the comma to distinguish a tuple
    def put(self, request, pk):
        photo = get_object_or_404(self.request.user.owner_photos, pk=pk)
        if 'file' not in request.data:
            raise ParseError('empty content')
        
        file = request.data['file']
        photo.photo.save(file.name, file, save=True)
        return Response(status=status.HTTP_200_OK)

class PhotoListView(generics.ListCreateAPIView):
    serializer_class = PhotoSerializer
    def get_queryset(self):
        return self.request.user.owner_photos

class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
