from django.shortcuts import render
from django.http import HttpRequest


def market_home(request: HttpRequest):
    return render(request, "market/market.html")
