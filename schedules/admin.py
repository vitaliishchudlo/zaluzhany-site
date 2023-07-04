from django.contrib import admin
from .models import Route, BusSchedule, ChurchSchedule

admin.site.register(Route)
admin.site.register(BusSchedule)
admin.site.register(ChurchSchedule)