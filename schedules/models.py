from django import forms
from django.db import models
from django.utils import timezone


class Route(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BusSchedule(models.Model):
    route_start = models.CharField(verbose_name="Початок маршруту", max_length=100, editable=True, blank=False,
                                   default="Дрогобич")
    route_end = models.ForeignKey(Route, verbose_name="Кінець маршруту", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Опис маршруту")
    images = models.ImageField(verbose_name="Картинки", upload_to='schedule/bus')
    notes = models.TextField(verbose_name="Примітки", blank=True, null=True)

    def __str__(self):
        return f"Відправлення з: {self.route_start} прибуття в: {self.route_end.name}"

    class Meta:
        verbose_name = 'Автобусний розклад'
        verbose_name_plural = 'Автобусні розклади'


class ChurchSchedule(models.Model):
    date_from = forms.DateField(initial=timezone.now, input_formats=['%d-%m-%Y', '%Y-%m-%d'])
    date_to = forms.DateField(input_formats=['%d-%m-%Y', '%Y-%m-%d'])
    images = models.ImageField(upload_to='schedule/church')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Church Schedule from {self.date_from} to {self.date_to}"

    class Meta:
        verbose_name = 'Церковний розклад'
        verbose_name_plural = 'Церковний розклад'
