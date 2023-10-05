from django.urls import path

from .views import users, playlists, animes, comments, ratings

# all these paths are prefaced by api/
# from AnimeOasis.urls.py

urlpatterns = [
    path("users/all/", users.user_list, name="all_users"),
    path("users/<int:pk>/", users.user_detail, name="user_by_id"),
]
