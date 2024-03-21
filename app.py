from flask import Flask, redirect, render_template, request, abort

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    return render_template('get_single_movie.html')


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    title = request.form.get('title')
    director = request.form.get('director')
    rating = request.form.get('rating')
    
    if not title:
        abort(400, description="Title is required")
    if not director:
        abort(400, description="Director is required")
    if not rating:
        abort(400, description="Rating is required")

    if not rating.isdigit():
        abort(400, description="Invalid rating format")

    rating = int(rating)

    movie = movie_repository.get_movie_by_id(movie_id)
    if not movie:
        abort(404, description="Movie not found")

    duplicate_movie = movie_repository.get_movie_by_title(title)
    if duplicate_movie and duplicate_movie.id != movie_id:
        abort(409, description="Duplicate movie title")

    movie.title = title
    movie.director = director
    movie.rating = rating
    movie_repository.update_movie(movie)
    
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
