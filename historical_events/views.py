from django.shortcuts import render


def home(request):
    context = {
        'title': 'Historical Events Home',
        'content': 'This is the content for the Historical Events Home Page.',
    }
    return render(request, 'historical_events/home.html', context)
