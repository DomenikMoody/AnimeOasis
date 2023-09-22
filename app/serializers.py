from rest_framework import serializers
from app.models import Anime, User, Comment, Rating, Playlist


# The serializers convert database model instances
# Into JSON, or vice versa
# IMPORTANT: We can use these to create new model instances from validated data
# https://www.django-rest-framework.org/tutorial/1-serialization/
# ModelSerializer comes with a lot of abstracted functionality
# Including methods for creating/deleting
class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'external_api_id']
        # TODO: figure out Anime model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','hashed_password','bio','display_name','favorite_show']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'show', 'author', 'content']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'show', 'user', 'star_rating']


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'playlist_name', 'summary', 'user', 'episodes']
