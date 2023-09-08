from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Waddup Otakus. You're at the AnimeOasis index.")
