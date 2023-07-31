from django.db import models
from django.utils import timezone


class BusSchedule(models.Model):
    ROUTE_CHOICES = [
        ('Залужани', 'Залужани'),
        ('Воля Якубова', 'Воля Якубова'),
        ('Снятинка', 'Снятинка'),
        ('Старе Село', 'Старе Село'),
        ('Рихтичі', 'Рихтичі'),
    ]

    route_start = models.CharField(verbose_name="Початок маршруту", max_length=100, editable=True, blank=False,
                                   default="Дрогобич")
    route_end = models.CharField(verbose_name="Кінець маршруту", choices=ROUTE_CHOICES, max_length=100)
    content = models.TextField(verbose_name="Опис маршруту")
    image = models.ImageField(verbose_name="Фотографії", upload_to='schedule/bus')
    notes = models.TextField(verbose_name="Примітки", blank=True, null=True)

    def __str__(self):
        return f"Відправлення з {self.route_start} прибуття в {self.route_end}"

    class Meta:
        verbose_name = 'Автобусний розклад'
        verbose_name_plural = 'Автобусні розклади'
        db_table = 'schedules_bus'


class ChurchSchedule(models.Model):
    date_from = models.DateField(verbose_name="Актуально від", default=timezone.now)
    date_to = models.DateField(verbose_name="Актуально до", default=timezone.now)
    notes = models.TextField(verbose_name="Примітки", blank=True, null=True)

    # images = models.ImageField(verbose_name="Фотографії", upload_to='schedule/church')

    def __str__(self):
        return f"Церковий розклад від {self.date_from} до {self.date_to}"

    class Meta:
        verbose_name = 'Церковний розклад'
        verbose_name_plural = 'Церковний розклад'
        db_table = 'schedules_church'


class ChurchScheduleImage(models.Model):
    schedule = models.ForeignKey(ChurchSchedule, on_delete=models.CASCADE, related_name='church_schedule_images')
    images = models.ImageField(verbose_name="Фотографія", upload_to='schedule/church')

    def __str__(self):
        return f"Фотографія для Церковного розкладу {self.schedule}"

    class Meta:
        db_table = 'schedules_church_images'
