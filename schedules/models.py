from django.db import models
from django.utils import timezone


class BusSchedule(models.Model):
    ROUTE_CHOICES = [
        ('Залужани', 'Залужани'),
        ('Воля Якубова', 'Воля Якубова'),
        ('Снятинка', 'Снятинка'),
        ('Рихтичі', 'Рихтичі'),
    ]

    route_start = models.CharField(verbose_name="Початок маршруту", max_length=100, editable=True, blank=False,
                                   default="Дрогобич")
    route_end = models.CharField(verbose_name="Кінець маршруту", choices=ROUTE_CHOICES, max_length=100)
    content = models.TextField(verbose_name="Опис маршруту")
    images = models.ImageField(verbose_name="Фотографії", upload_to='schedule/bus')
    notes = models.TextField(verbose_name="Примітки", blank=True, null=True)

    def __str__(self):
        return f"Відправлення з {self.route_start} прибуття в {self.route_end}"

    class Meta:
        verbose_name = 'Автобусний розклад'
        verbose_name_plural = 'Автобусні розклади'


class ChurchSchedule(models.Model):
    date_from = models.DateField(verbose_name="Актуально від", default=timezone.now)
    date_to = models.DateField(verbose_name="Актуально до", default=timezone.now)
    images = models.ImageField(verbose_name="Фотографії", upload_to='schedule/church')
    notes = models.TextField(verbose_name="Примітки", blank=True, null=True)

    def __str__(self):
        return f"Церковий розклад від {self.date_from} до {self.date_to}"

    class Meta:
        verbose_name = 'Церковний розклад'
        verbose_name_plural = 'Церковний розклад'
