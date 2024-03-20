# Feature 2

from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository


movie_repository = get_movie_repository()

def test_create_page(test_app: FlaskClient):
    response = test_app.get("/movies/new")
    
    assert b'<form method="POST" action="/movies" class="container">' in response.data
    assert b'<input type="submit" value="Submit" class="btn btn-primary">' in response.data
    
    assert response.status_code == 200
    
def test_create_movie(test_app: FlaskClient):
    response = test_app.post('/movies', data = {
        'title': "Self",
        'director': "Searit Huluf",
        'rating': 2})
    
    assert response
    # we check for a 302 status code because we are redirecting to the /movies page
    # we would have a 200 status code when we follow the redirect and the other tests pass i believe
    assert response.status_code == 302
    
# a rating can be bad by not being an int or being outside the range of 1-5
def test_create_movie_bad_rating(test_app: FlaskClient):
    response = test_app.post('/movies', data = {
        'title': "Self",
        'director': "Searit Huluf",
        'rating': 6})
    
    assert response
    assert response.status_code == 400
    
def test_create_movie_bad_title(test_app: FlaskClient):
    response = test_app.post('/movies', data = {
        'title': None,
        'director': "Searit Huluf",
        'rating': 2})
    
    assert response
    assert response.status_code == 400
    
def test_create_movie_bad_director(test_app: FlaskClient):
    response = test_app.post('/movies', data = {
        'title': "Self",
        'director': None,
        'rating': 2})
    
    assert response
    assert response.status_code == 400