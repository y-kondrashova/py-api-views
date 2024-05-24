from django.urls import path

from cinema.views import (
    ActorDetail,
    ActorList,
    CinemaHallList,
    GenreDetail,
    GenreList,
    movie_detail,
    movie_list
)

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path(
        "cinema-halls/",
        CinemaHallList.as_view(actions={"get": "list", "post": "create"}),
        name="cinema-hall-list"
    ),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]

app_name = "cinema"
