# Generated by Django 4.1.5 on 2023-07-09 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historical_events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='historicalevent',
            table='historical_events_historical_event',
        ),
    ]
