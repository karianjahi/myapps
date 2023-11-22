from django.db import models


class Artist(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField(default="unknown")

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['created_on']


class Album(models.Model):
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
