from django.shortcuts import render


def home(request):
    context = {
        'title_variable': 'Historical Events Home',
        'content_variable': 'This is the content for the Historical Events Home Page.',
    }
    return render(request, 'historical_events/home.html', context)
