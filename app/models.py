from django.db import models

# Create your models here.
# If a model does not have an attribute
# with primary_key = True,
# it automatically assigns an autoincrementing integer field
# IMPORTANT:
#   The order of model classes matters,
#   bc a related model must be defined before the model
#   that references it

class Anime(models.Model):
    pass

class User(models.Model):
    username = models.CharField("username", max_length=100, unique=True)
    hashed_password = models.CharField("password", max_length=50)
    bio = models.CharField("bio", max_length=500)
    display_name = models.CharField(max_length=100, unique=False)
    favorite_show = models.OneToOneField(
        Anime,
    )


class Playlist(models.Model):
    pass

class Comment(models.Model):
    pass

class Review(models.Model):
    pass
