from django.urls import path

from . import views

# all these paths are prefaced by api/
# from AnimeOasis.urls.py

urlpatterns = [
    path("", views.index, name="index"),
]
