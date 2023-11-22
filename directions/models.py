from django.db import models


class Direction(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    origin = models.TextField()
    destination = models.TextField()
    distance = models.CharField(max_length=100, blank=True)
    duration = models.CharField(max_length=100, blank=True)





