# from django.contrib import admin
#
# from .models import BusSchedule, ChurchSchedule, ChurchScheduleImage
#
#
# class BusScheduleAdmin(admin.ModelAdmin):
#     readonly_fields = ('route_start',)
#     fields = ('route_start', 'route_end', 'content', 'images', 'notes')
#
#
# admin.site.register(BusSchedule, BusScheduleAdmin)
# admin.site.register(ChurchSchedule)
# admin.site.register(ChurchScheduleImage)


from django.contrib import admin
from .models import BusSchedule, ChurchSchedule, ChurchScheduleImage


class ChurchScheduleImageInline(admin.TabularInline):
    model = ChurchScheduleImage


class ChurchScheduleAdmin(admin.ModelAdmin):
    inlines = [ChurchScheduleImageInline]
    readonly_fields = ('date_from', 'date_to')
    fields = ('date_from', 'date_to', 'notes')


class BusScheduleAdmin(admin.ModelAdmin):
    readonly_fields = ('route_start',)
    fields = ('route_start', 'route_end', 'content', 'image', 'notes')


admin.site.register(ChurchSchedule, ChurchScheduleAdmin)
admin.site.register(BusSchedule, BusScheduleAdmin)
