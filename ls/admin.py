from django.contrib import admin

from .models import Anime, Playlist, User, Comment, Rating
# Register your models here.
# This lets us play with our data on the admin site
admin.site.register([
    Anime, Playlist, User, Comment, Rating
])
