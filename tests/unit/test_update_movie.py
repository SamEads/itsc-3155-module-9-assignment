# TODO: Feature 5
import pytest
from app.py import app


def test_create_movie(test_app: FlaskClient):
    response = FlaskClient.post('/movies/1', data={"title": "New Movie Title", "director": "New Director", "rating": "5"})
    assert response.status_code == 302

def test_update_movie(test_app: FlaskClient):
    response_create = client.post('/movies')
    assert response_create.status_code == 302

    response = client.post('/movies/1', data={"title": "Updated Movie Title", "director": "Updated Director", "rating": "4"})
    assert response.status_code == 302