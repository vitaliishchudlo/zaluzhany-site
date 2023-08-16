# Generated by Django 4.1.5 on 2023-07-09 19:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_start', models.CharField(default='Дрогобич', max_length=100, verbose_name='Початок маршруту')),
                ('route_end', models.CharField(choices=[('Залужани', 'Залужани'), ('Воля Якубова', 'Воля Якубова'), ('Снятинка', 'Снятинка'), ('Рихтичі', 'Рихтичі')], max_length=100, verbose_name='Кінець маршруту')),
                ('content', models.TextField(verbose_name='Опис маршруту')),
                ('img', models.ImageField(upload_to='schedule/bus', verbose_name='Фотографії')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Примітки')),
            ],
            options={
                'verbose_name': 'Автобусний розклад',
                'verbose_name_plural': 'Автобусні розклади',
            },
        ),
        migrations.CreateModel(
            name='ChurchSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(default=django.utils.timezone.now, verbose_name='Актуально від')),
                ('date_to', models.DateField(default=django.utils.timezone.now, verbose_name='Актуально до')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Примітки')),
            ],
            options={
                'verbose_name': 'Церковний розклад',
                'verbose_name_plural': 'Церковний розклад',
            },
        ),
        migrations.CreateModel(
            name='ChurchScheduleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='schedule/church', verbose_name='Фотографія')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='church_schedule_images', to='schedules.churchschedule')),
            ],
        ),
    ]
