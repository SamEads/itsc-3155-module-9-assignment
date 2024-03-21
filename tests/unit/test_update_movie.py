# TODO: Feature 5
import pytest
from flask import request
from app import app
from flask.testing import FlaskClient
from app import app

@pytest_fixture
def test_app() -> FlaskClient:
    app = create_app()
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client

def test_create_movie(test_app: FlaskClient):
    response = test_app.post('/movies/1', data={"title": "New Movie Title", "director": "New Director", "rating": "5"})
    assert response.status_code == 302

def test_update_movie(test_app: FlaskClient):
    response_create = test_app.post('/movies')
    assert response_create.status_code == 404

    response = test_app.post('/movies/1', data={"title": "Updated Movie Title", "director": "Updated Director", "rating": "4"})
    assert response.status_code == 404

def test_get_movie(test_app: FlaskClient):
    response = test_app.get('/movies/1')
    assert response.status_code == 404

def test_delete_movie(test_app: FlaskClient):
    response = test_app.delete('/movies/1')
    assert response.status_code == 404

def test_list_movies(test_app: FlaskClient):
    response = test_app.get('/movies')
    assert response.status_code == 200

def test_invalid_create_movie(test_app: FlaskClient):
    response = test_app.post('/movies', data={"title": "", "director": "Invalid Director", "rating": "Invalid Rating"})
    assert response.status_code == 400

