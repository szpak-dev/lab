from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello from Food Factory Django')
