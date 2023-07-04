from django.db import models
from django.utils import timezone


# Create your models here.

class HistoricalEvent(models.Model):
    event_date = models.DateField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} | {self.event_date}'
