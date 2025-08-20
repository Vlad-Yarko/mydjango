from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("query", views.query, name="query"),
    path("<str:name>", views.name, name="name")
]
