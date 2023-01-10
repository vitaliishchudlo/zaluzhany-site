from django.db import models


class HistoricalEvents(models.Model):
    event_year = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
