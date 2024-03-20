# TODO: Feature 5
import pytest
from app.py import app
from app.py.src.models import Movie
from app.py.src.repositories.movie_repository import get_movie_repository
from flask.testing import FlaskClient

movie_repository = get_movie_repository()

def test_edit_movie_page(test_app: FlaskClient):
   response = test_app.get('/movies/1/edit')
   assert response.status_code == 200
   assert b'<h1>Edit Movie</h1>' in response.data
   data = {
        'title': 'The Godfather',
        'director': 'Franis Coppola',
        'rating': '5'
    }
   response = client.post('/movies/1', data=data, follow_redirects=True)

   assert response.status_code == 200

   assert b"The Godfather" in response.data
   assert b"Francis Coppola" in response.data
   assert b"5" in response.data
    
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
    response = test_app.get('/movies/999/edit')

    assert response.status_code == 401
    assert b"Unauthorized" in response.data

def test_duplicate_movie_title(test_app: FlaskClient):
    data = {
        'title': 'The Godfather',
        'director': 'Franics Coppola',
        'rating': '5'
    }

    response = test_app.post('/movies/1', data=data, follow_redirects=True)

    assert response.status_code == 409
    assert b"Conflict" in response.data
    assert b"A movie with the same title already exists" in response.data

def test_edit_non_existent_movie(test_app: FlaskClient):
    response = test_app.get('/movies/999/edit')
    assert response.status_code == 404
    assert b"Not Found" in response.data
    assert b"Movie not found" in response.data

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