import json

from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Author, Post, User, Profile, Student, Course


# One to many / many `to one
@method_decorator(csrf_exempt, name='dispatch')
class AuthorView(View):
    def get(self, request: HttpRequest):
        id = request.GET.get('id')
        if id:
            authors_data = Author.objects.filter(id=id)
        else:
            authors_data = Author.objects.all()[10:20]
        data = dict()
        for author in authors_data:
            data[author.id] = list(author.posts.values())
        return JsonResponse({
            "data": data
        })
    
    @csrf_exempt
    def post(self, request: HttpRequest):
        raw_data = request.body
        data = json.loads(raw_data)
        # validation
        author = Author(**data)
        author.save()
        return JsonResponse({"data": data})
    
    @csrf_exempt
    def put(self, request: HttpRequest):
        raw_data = request.body
        data = json.loads(raw_data)
        # validation
        author = Author.objects.get(id=data.get("id"))
        author.name = "bobi"
        author.save()
        # Author.objects.filter(id=data.get("id")).update(**data)
        return JsonResponse({"data": data})
    
    @csrf_exempt
    def delete(self, request: HttpRequest):
        raw_data = request.body
        data = json.loads(raw_data)
        # validation
        Author.objects.filter(id=data.get("id")).delete()
        return JsonResponse({"data": data})
