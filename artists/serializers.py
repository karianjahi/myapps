from rest_framework import serializers
from artists.models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "created_on", "first_name", "last_name", "address"]


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["artist_id", "name"]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["album_id", "name"]
