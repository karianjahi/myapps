from django.urls import path, include
from artists import views


urlpatterns = [
    path('artists/', views.ArtistList.as_view()),
    path('artists/<int:pk>', views.ArtistDetail.as_view()),
    path('artists/albums/', views.AlbumList.as_view()),
    path('artists/albums/<int:pk>', views.AlbumDetail.as_view()),
    path('artists/albums/songs/', views.SongList.as_view()),
    path('artists/albums/songs/<int:pk>', views.SongDetail.as_view()),
]