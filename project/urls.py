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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('addalbum/', views.AddAlbum, name='add_album'),
    path('albumlist/', views.AlbumList.as_view(), name='album_list'),
    path('addphoto/', views.AddPhoto.as_view(), name='add_photo'),
    path('photolist/', views.PhotoList.as_view(), name='photo_list'),
    path('albumview/',views.AlbumView.as_view(), name='album_view'),
    path('addcomment/', views.AddComment.as_view(), name='add_comment'),
    path('viewcomment/', views.CommentListView.as_view(), name='view_comment'),
    path('editalbum/', views.EditAlbum.as_view(), name='edit_album')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
