from django.shortcuts import render
from django.http import HttpRequest
from django.views import View


def home(request: HttpRequest):
    context = {
        "special_header": "Special header"
    }
    return render(request, "base/home.html", context)


def name(request: HttpRequest, name):
    context = {
        "name": name
    }
    return render(request, "base/name.html", context)


def query(request: HttpRequest):
    if request.method == "GET": 
        context = {
            "query": request.GET.get("query", "No query")
        }
        print(context)
        return render(request, "base/query.html", context)
    else:
        print("POST")
        
        
class PukView(View):
    def get(self, request: HttpRequest):
        return render(request, "base/puk.html")
