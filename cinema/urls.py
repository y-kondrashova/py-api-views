from django.urls import path

from cinema.views import (
    GenreDetail,
    GenreList,
    movie_list,
    movie_detail
)

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
