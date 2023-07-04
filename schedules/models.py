from django.db import models
from django.utils import timezone

class Route(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BusSchedule(models.Model):
    route_start = models.CharField(max_length=100, default="Дрогобич", editable=False)
    route_end = models.ForeignKey(Route, on_delete=models.CASCADE)
    content = models.TextField()
    images = models.ImageField(upload_to='schedule/bus')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Schedule from {self.route_start} to {self.route_end.name}"


class ChurchSchedule(models.Model):
    date_from = models.DateField(default=timezone.now, input_formats=['%d-%m-%Y', '%Y-%m-%d'])
    date_to = models.DateField(input_formats=['%d-%m-%Y', '%Y-%m-%d'])
    images = models.ImageField(upload_to='schedule/church')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Church Schedule from {self.date_from} to {self.date_to}"
