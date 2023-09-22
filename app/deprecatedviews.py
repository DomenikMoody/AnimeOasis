from django.shortcuts import render
from django.http import HttpResponse
import requests
# This is the api
# Need to figure out how we getting CORS and stuff up in here

# TODO: Delete this file lol

def index(request):
    return HttpResponse("Waddup Otakus. You're at the AnimeOasis index.")

def testSearch(request):
    url = f'https://api.consumet.org/anime/gogoanime/demon'
    response = requests.get(url, params={"page": 2})
    data = response.json()
    print(data)
    return HttpResponse(f'{data}')
