from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
# If a model does not have an attribute
# with primary_key = True,
# it automatically assigns an autoincrementing integer field
# IMPORTANT:
#   The order of model classes matters,
#   bc a related model must be defined before the model
#   that references it

class Anime(models.Model):
    external_api_key = models.CharField(primary_key=True)
    # I think all we need is the api key?
    # unless we want to collect more data on each anime
    # as users query the external api for them
    def get_average_rating(self):
        """
        Queries for all of an anime's ratings
        and returns the average rating
        """
        # TODO: Implement this function so we can use
        #  Anime.get_average_rating in the Views
        pass



class User(models.Model):
    username = models.CharField("username", max_length=100, unique=True)
    hashed_password = models.CharField("password", max_length=50)
    bio = models.CharField("bio", max_length=500)
    display_name = models.CharField(max_length=100, unique=False)
    favorite_show = models.ForeignKey(
        Anime,
        on_delete=models.SET_NULL,
    )
    # models.ForeignKey defines a many-to-one relationship;
    # A user has one favorite anime,
    # but one anime can be favorited by many users

class Comment(models.Model):
    show = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    content = models.CharField(max_length=250)



def validate_rating(val):
        if 1 <= val <= 5:
            return val
        else:
            raise ValidationError("Ratings must be an integer between 1 and 5")

class Rating(models.Model):

    show = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    star_rating = models.IntegerField(validators=[validate_rating])


class Playlist(models.Model):
    pass
