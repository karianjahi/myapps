from django.db import models
from league.epl import Table

seasons = Table().table["Season"].unique()
seasons = [(i, i) for i in seasons]


class Season(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    season = models.CharField(max_length=40, choices=seasons)
    winner = models.CharField(max_length=40, blank=True)
    second = models.CharField(max_length=40, blank=True)
    third = models.CharField(max_length=40, blank=True)
    fourth = models.CharField(max_length=40, blank=True)
    first_relegated = models.CharField(max_length=40, blank=True)
    second_relegated = models.CharField(max_length=40, blank=True)
    third_relegated = models.CharField(max_length=40, blank=True)
    owner = models.ForeignKey('auth.User',
                              related_name="season",
                              on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["created_on", "season"]
