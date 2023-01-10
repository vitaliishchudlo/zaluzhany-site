from django.urls import path

from historical_events.views import index, second

urlpatterns = [
    path('', index),
    path('test/<int:catid>/', second),
]
