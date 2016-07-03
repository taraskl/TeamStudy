from django.shortcuts import render

from django.http import HttpResponse


def index3(request):
    return HttpResponse("Hello, world. You're at the pizza_service index.")


# Create your views here.
