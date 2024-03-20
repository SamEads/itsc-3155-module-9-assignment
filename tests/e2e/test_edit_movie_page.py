# TODO: Feature 5
import pytest
from app.py import app
from app.py.src.models import Movie
from app.py.src.repositories.movie_repository import get_movie_repository
from flask.testing import FlaskClient

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
    