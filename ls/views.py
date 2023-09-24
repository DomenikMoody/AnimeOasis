from django.shortcuts import render
from django.http import HttpResponse

# This is the api
# Need to figure out how we getting CORS and stuff up in here

def index(request):
    return HttpResponse("Waddup Otakus. You're at the AnimeOasis index.")
