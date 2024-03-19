# TODO: Feature 5
import pytest
from app.py import app
from app.py.src.models import Movie
from app.py.src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_edit_movie_page():
   response = client.get('/movies/1/edit')
   assert response.status_code == 200
   assert b'<h1>Edit Movie</h1>' in response.data
   data = {
        'title': 'The Godfather',
        'genre': 'Crime',
        'released_year': 1972
    }
   resonse = client.post('/movies/1', data=data, follow_redirects=True)

   assert response.status_code == 200

   assert b"New Movie Title" in response.data
   assert b"New Movie Genre" in response.data
   assert b"2022" in response.data
    