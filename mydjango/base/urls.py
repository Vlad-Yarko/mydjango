from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("query", views.query, name="query"),
    path("puk", views.PukView.as_view(), name="puk"),
    path("<str:name>", views.name, name="name")
]
