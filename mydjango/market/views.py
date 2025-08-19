from django.http import HttpResponse
from django.http.request import HttpRequest


def home(request: HttpRequest):
    return HttpResponse("Home page")
