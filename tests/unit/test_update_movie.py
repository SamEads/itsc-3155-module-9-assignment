# TODO: Feature 5
import requests

def test_update_movie():
    url = "http://localhost:5000/movies/1"

    new_movie_data = {
        "title": "New Movie Title",
        "director": "New Director",
        "rating": "5"
    }

    response = requests.post(url, data=new_movie_data)

    assert response.status_code == 200

    updated_movie = response.json()
    assert updated_movie["title"] == new_movie_data["title"]
    assert updated_movie["director"] == new_movie_data["director"]
    assert updated_movie["rating"] == new_movie_data["rating"]