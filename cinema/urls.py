from django.urls import path

from cinema.views import (
    ActorList,
    GenreDetail,
    GenreList,
    movie_list,
    movie_detail
)

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
