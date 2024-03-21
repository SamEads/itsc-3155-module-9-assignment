# TODO: Feature 5
import pytest
from flask import request
from app import app
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository
from flask.testing import FlaskClient
from app import movie_repository


movie_repository = get_movie_repository()

@pytest.fixture
def movie_repository():
    return MovieRepository

def test_edit_movie_page(test_app: FlaskClient):
   response = test_app.get('/movies/1/edit')
   assert response.status_code == 200
   assert b'<h1 class="mb-5">Edit Movie</h1>' in response.data
   assert b'Title' in response.data
   assert b'Director' in response.data
   assert b'Rating' in response.data
      
def test_invalid_movie_edit(test_app: FlaskClient):
    data = { 
        'title': '',
        'director': 'Franics Coppola',
        'rating': '5'
    }

    response = test_app.post('/movies/1', data=data, follow_redirects=True)

    assert response.status_code == 400
    assert b"Bad Request" in response.data
    assert b"Title is required" in response.data

def test_movie_not_found(test_app: FlaskClient):
    response = test_app.post('/movies/999', data={'title': 'New Title', 'director': 'New Director', 'rating': '5'})

    assert response.status_code == 404

def test_duplicate_movie_title(test_app: FlaskClient, movie_repository):
    movie_repository.create(Movie(1, 'Existing Moive', 'Existing Director', 3))
    data = {
        'title': 'The Godfather',
        'director': 'Franics Coppola',
        'rating': '5'
    }

    response = test_app.post('/movies/1', data=data, follow_redirects=True)

    assert response.status_code == 409
   

def test_edit_non_existent_movie(test_app: FlaskClient):
    movie = movie_repository.get_movie_by_id(999)
    if movie:
        movie_repository.delete(999)

    response = test_app.get('/movies/999', data={'title': 'New Title', 'director': 'New Director', 'rating': '5'})
    assert response.status_code == 404
    

def test_invalid_input_format(test_app: FlaskClient):
    data = {
        'title': 'The Godfather',
        'director': 'Francis Coppola',
        'rating': 'InvalidRating'
    }
    response = test_app.post('/movies/1', data=data, follow_redirects=True)

    assert response.status_code == 400
    assert b"Bad Request" in response.data
    assert b"Invalid rating format" in response.data