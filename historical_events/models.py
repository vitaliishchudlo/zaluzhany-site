from django.db import models
from django.utils import timezone
from django import forms


class HistoricalEvent(models.Model):
    event_date = forms.DateField(input_formats=['%d-%m-%Y', '%Y-%m-%d'])
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} | {self.event_date}'
