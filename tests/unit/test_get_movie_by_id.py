# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id_alternative():
    # Create test movies
    movies_data = [
        {'title': 'Damsel', 'director': 'Mark Zuck', 'rating': 2},
        {'title': 'The Great Gatsby', 'director': 'Baz Luhrmann', 'rating': 4},
        {'title': 'Dune 2', 'director': 'Denis Villeneuve', 'rating': 4},
        {'title': 'Dune 1', 'director': 'Denis Villeneuve', 'rating': 1}
    ]
    # Store movie ids for later comparison
    movie_ids = []
    # Create and retrieve movies
    for movie_data in movies_data:
        movie_repository = get_movie_repository()
        movie_repository.create_movie(movie_data['title'], movie_data['director'], movie_data['rating'])
        movie = movie_repository.get_movie_by_title(movie_data['title'])
        assert movie.title == movie_data['title']
        assert movie.director == movie_data['director']
        assert movie.rating == movie_data['rating']
        movie_ids.append(movie.movie_id)
    # Verify retrieval by ID
    for i in range(len(movies_data)):
        movie_repository = get_movie_repository()
        movie = movie_repository.get_movie_by_id(movie_ids[i])
        assert movie.title == movies_data[i]['title']
        assert movie.director == movies_data[i]['director']
        assert movie.rating == movies_data[i]['rating']

