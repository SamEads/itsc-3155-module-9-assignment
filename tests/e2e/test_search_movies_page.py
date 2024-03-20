import pytest
from flask import request
from app import app
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture
def client():
    app.config['TESTING'] = True    # Set the app to testing mode
    with app.test_client() as client:   # Create a test client using the Flask application
        yield client    # begin testing

#search without title
def test_search_movies_without_title(client):   # define test environment
    """Test the search_movies route without a title"""

    sim_repo = get_movie_repository()    #create a fake repo, empty

    #test empty title backend
    response = client.get('/movies/search')   #pass empty title to search
    assert response.status_code == 200  # page exists

    #test empty title frontend
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response.data
    assert b'<p>No matches found</p>' in response.data



#search with title
def test_search_movies_with_title(client):    # define test environment
    """Test the search_movies route"""
    
    #define mock movie repository
    sim_repo = get_movie_repository()    #create a fake repo, empty

    #set sim_repo contents
    movie1 = Movie(1, title='Inception', director= 'Christopher Nolan', rating = 8.8)
    movie2 = Movie(2, title='The Godfather', director= 'Francis Ford Coppola', rating = 9.2)
    movie3 = Movie(3, title='The Shawshank Redemption', director= 'Frank Darabont', rating = 9.3)
    movie4 = Movie(4, title='Pulp Fiction', director= 'Quentin Tarantino', rating = 8.9)
    movie5 = Movie(5, title='The Dark Knight', director= 'Christopher Nolan', rating = 9.0)
    movie6 = Movie(6, title='Fight Club', director= 'David Fincher', rating = 8.8)
    movie7 = Movie(7, title='Forrest Gump', director= 'Robert Zemeckis', rating = 8.8)

    sim_repo._db = {1: movie1, 2: movie2, 3: movie3, 4: movie4, 5: movie5, 6: movie6, 7: movie7}    #set sim_repo contents


    #test known title backend
    response = client.get('/movies/search?title=Inception')     #pass known title to search
    assert response.status_code == 200  # page exists

    #test known title frontend
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response.data
    assert b'<p class="card-text">Director: Christopher Nolan</p>' in response.data
    assert b'<p class="card-text">Rating: 8.8</p>' in response.data


#search with non-existent title
def test_search_movies_nonexistent_title(client):
    """Test the search_movies route with a non-existent title"""
    
    #define mock movie repository
    sim_repo = get_movie_repository()    #create a fake repo, empty

    #set sim_repo contents
    movie1 = Movie(1, title='Inception', director= 'Christopher Nolan', rating = 8.8)
    movie2 = Movie(2, title='The Godfather', director= 'Francis Ford Coppola', rating = 9.2)
    movie3 = Movie(3, title='The Shawshank Redemption', director= 'Frank Darabont', rating = 9.3)
    movie4 = Movie(4, title='Pulp Fiction', director= 'Quentin Tarantino', rating = 8.9)
    movie5 = Movie(5, title='The Dark Knight', director= 'Christopher Nolan', rating = 9.0)
    movie6 = Movie(6, title='Fight Club', director= 'David Fincher', rating = 8.8)
    movie7 = Movie(7, title='Forrest Gump', director= 'Robert Zemeckis', rating = 8.8)

    sim_repo._db = {1: movie1, 2: movie2, 3: movie3, 4: movie4, 5: movie5, 6: movie6, 7: movie7}    #set sim_repo contents

    # test non-existent title backend
    response = client.get('/movies/search?title=NonExistentTitle')
    assert response.status_code == 200  # page exists

    # test non-existent title frontend
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response.data
    assert b'<p>No matches found</p>' in response.data


#search with special characters
def test_search_movies_with_special_characters(client):
    """Test the search_movies route with a title containing special characters"""
    
    #define mock movie repository
    sim_repo = get_movie_repository()    #create a fake repo, empty

    #set sim_repo contents
    movie1 = Movie(1, title='Inception', director= 'Christopher Nolan', rating = 8.8)
    movie2 = Movie(2, title='The Godfather', director= 'Francis Ford Coppola', rating = 9.2)
    movie3 = Movie(3, title='The Shawshank Redemption', director= 'Frank Darabont', rating = 9.3)
    movie4 = Movie(4, title='Pulp Fiction', director= 'Quentin Tarantino', rating = 8.9)
    movie5 = Movie(5, title='The Dark Knight', director= 'Christopher Nolan', rating = 9.0)
    movie6 = Movie(6, title='Fight Club', director= 'David Fincher', rating = 8.8)
    movie7 = Movie(7, title='Forrest Gump', director= 'Robert Zemeckis', rating = 8.8)

    sim_repo._db = {1: movie1, 2: movie2, 3: movie3, 4: movie4, 5: movie5, 6: movie6, 7: movie7}    #set sim_repo contents

    # test title with special characters backend
    response = client.get('/movies/search?title=The%20Dark%20Knight')
    assert response.status_code == 200  # page exists

    # test title with special characters frontend
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response.data
    assert b'<p class="card-text">Director: Christopher Nolan</p>' in response.data
    assert b'<p class="card-text">Rating: 9.0</p>' in response.data


#search with empty title
def test_search_movies_empty_title_parameter(client):
    """Test the search_movies route without providing a title parameter"""
    
    #define mock movie repository
    sim_repo = get_movie_repository()    #create a fake repo, empty

    #set sim_repo contents
    movie1 = Movie(1, title='Inception', director= 'Christopher Nolan', rating = 8.8)
    movie2 = Movie(2, title='The Godfather', director= 'Francis Ford Coppola', rating = 9.2)
    movie3 = Movie(3, title='The Shawshank Redemption', director= 'Frank Darabont', rating = 9.3)
    movie4 = Movie(4, title='Pulp Fiction', director= 'Quentin Tarantino', rating = 8.9)
    movie5 = Movie(5, title='The Dark Knight', director= 'Christopher Nolan', rating = 9.0)
    movie6 = Movie(6, title='Fight Club', director= 'David Fincher', rating = 8.8)
    movie7 = Movie(7, title='Forrest Gump', director= 'Robert Zemeckis', rating = 8.8)

    sim_repo._db = {1: movie1, 2: movie2, 3: movie3, 4: movie4, 5: movie5, 6: movie6, 7: movie7}    #set sim_repo contents

    # test empty title parameter backend
    response = client.get('/movies/search?title=')
    assert response.status_code == 200  # page exists

    # test empty title parameter frontend
    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response.data
    assert b'<p>No matches found</p>' in response.data.strip()
