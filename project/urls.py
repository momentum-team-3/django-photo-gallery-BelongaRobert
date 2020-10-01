"""project URL Configuration

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from gallery import views
from api import views as api_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('addalbum/', views.AddAlbum.as_view(), name='add_album'),
    path('albumlist/', views.AlbumList.as_view(), name='album_list'),
    path('list_all_albums/', views.list_all_albums.as_view(), name='list_all_albums'),
    path('addphoto/', views.AddPhoto.as_view(), name='add_photo'),
    path('photo/list/<int:pk>', views.PhotoList.as_view(), name='photo_list'),
    path('album/view/<int:pk>',views.AlbumView.as_view(), name='album_view'),
    path('addcomment/', views.AddComment.as_view(), name='add_comment'),
    path('view_comment/', views.CommentListView.as_view(), name='view_comment'),
    path('album/edit/<int:pk>', views.EditAlbum, name='edit_album'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('userphotos/', views.UserPhotos.as_view(), name='user_photos'),
    path('photo/delete/', views.DeletePhoto.as_view(), name='delete_photo'),
# api urls #
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/albumlist/', api_views.AlbumListView.as_view(), name ='albumlistview'),
    path('api/albumlist/<int:pk>/', api_views.AlbumDetailView.as_view(), name = 'albumdetailview'),
    # path('api/photo/<int:pk>/', api_views.PhotoImageApiView.as_view()),
    # path('api/photo/', api_views.PhotoListView.as_view()),
    # path('api/photo/<int:pk>/', api_views.PhotoDetailView.as_view()),
    # path('api/auth/', include('djoser.urls')),
    # path('api/auth/', include('djoser.urls.authtoken')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
