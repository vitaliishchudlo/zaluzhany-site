from django.db import models
from django.utils import timezone

class HistoricalEvent(models.Model):
    event_date = models.DateField(default=timezone.now)
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} | {self.event_date}'

    class Meta:
        verbose_name = 'Історична подія'
        verbose_name_plural = 'Історичні події'
        db_table = 'historical_events_historical_event'
