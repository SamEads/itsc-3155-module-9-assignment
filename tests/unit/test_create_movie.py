# Feature 2
from src.repositories.movie_repository import get_movie_repository

def test_create_movie():
    movie_repository = get_movie_repository()
    title = "Title"
    director = "Director"
    rating = 1

    movie_repository.create_movie(title, director, rating)
    movie = movie_repository.get_movie_by_title(title) # get movie from repository instead of assigning beforehand
    assert movie is not None
    assert movie.title == title
    assert movie.director == director
    assert movie.rating == rating