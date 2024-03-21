# TODO: Feature 4
from flask.testing import FlaskClient
from app import app
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_view_movie_end_to_end_alternative(test_app: FlaskClient):
    # Create a test movie
    test_movie = {
        'title': 'Test Movie',
        'director': 'Test Director',
        'rating': 4
    }
    movie_repository.create_movie(test_movie['title'], test_movie['director'], test_movie['rating'])
    
    # Retrieve the test movie from the repository
    movie = movie_repository.get_movie_by_title(test_movie['title'])
    movie_id = movie.movie_id
    
    # Send a request to view the movie
    response = test_app.get(f'/movies/{movie_id}')
    
    # Check if the response is successful and contains the expected movie details
    assert response.status_code == 200
    assert test_movie['title'] in response.data.decode('utf-8')
    assert str(test_movie['rating']) in response.data.decode('utf-8')
    assert test_movie['director'] in response.data.decode('utf-8')
    assert f'action="/movies/{movie_id}/edit"' in response.data.decode('utf-8')
    assert f'action="/movies/{movie_id}/delete"' in response.data.decode('utf-8')