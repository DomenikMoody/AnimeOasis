from django.urls import path

from . import views

# all these paths are prefaced by api/
# from AnimeOasis.urls.py

urlpatterns = [
    path("", views.index, name="index"),
    path("users/", views.index, name="index"),
    path("comments/", views.index, name="index"),
    path("animes/", views.index, name="index"),
    path("playlists/", views.index, name="index"),
]
