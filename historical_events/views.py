from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import HistoricalEvents
import json
from django.core import serializers


def index(request):
    events = HistoricalEvents.objects.all()
    # events = serializers.serialize('json', events)
    return render(request, 'historical_events/index.html', {'events': events})

def about(request):
    # events = HistoricalEvents.objects.all()
    # events = serializers.serialize('json', events)
    return render(request, 'historical_events/index.html')
