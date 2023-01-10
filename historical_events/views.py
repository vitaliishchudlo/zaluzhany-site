from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Home page</h1>')


def second(request, catid):
    return HttpResponse(f'<h2>I am in second, ID - {catid}</h2>')
