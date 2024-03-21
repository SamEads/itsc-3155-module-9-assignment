# TODO: Feature 1

import pytest
from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository
import src.models.movie

@pytest.fixture()
def test_app():
    return app.test_client()

def test_no_movies_in_page(test_app : FlaskClient):
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')
    print(response_data)
    assert response.status_code == 200
    assert '<h1>There are no movies currently in our database :(</h1>' in response_data

def test_movies_in_page(test_app : FlaskClient):
    movies = get_movie_repository()
    movies.create_movie("Dune", "Denis Veinellel", 5)
    movies.create_movie("Star Wars", "George Lucas", 5)
    movies.create_movie("The Room", "???", 1)
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')
    assert response.status_code == 200
    movie_dict = movies.get_all_movies()
    for index, (movie_id, movie) in enumerate(movie_dict.items()):
        assert '<td class="element-style">' + str(movie_id) + '</td>' in response_data
        assert '<td class="element-style">' + movie.title + '</td>' in response_data
        assert '<td class="element-style">' + movie.director + '</td>' in response_data
        star_html = response_data.split('<td>')[index + 1]
        stars = star_html.count('<span class="star-style">★</span>')
        assert stars == movie.rating
        