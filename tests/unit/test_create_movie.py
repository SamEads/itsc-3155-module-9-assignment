# Feature 2
from flask import app
from flask.testing import FlaskClient
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

def test_create_movie():
    # Arrange
    movie_repository = get_movie_repository()
    title = "Title"
    director = "Director"
    rating = 1

    movie = movie_repository.create_movie(title, director, rating)

    assert isinstance(movie, Movie)
    assert movie.title == title
    assert movie.director == director
    assert movie.rating == rating # movie.rating >= 1 and movie.rating <= 5 ?