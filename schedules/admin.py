from django.contrib import admin

from .models import BusSchedule
from .models import Route, ChurchSchedule


class BusScheduleAdmin(admin.ModelAdmin):
    readonly_fields = ('route_start',)
    fields = ('route_start', 'route_end', 'content', 'images', 'notes')


admin.site.register(Route)
admin.site.register(BusSchedule, BusScheduleAdmin)
admin.site.register(ChurchSchedule)
