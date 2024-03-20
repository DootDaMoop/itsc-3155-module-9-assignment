from flask import Flask, redirect, render_template, request, url_for, abort

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')

movie_list = {}
@app.get('/movies')
def list_all_movies():
    movie_list = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', the_movie_list=movie_list)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    title = request.form['movieName']
    director = request.form['movieDirector']
    rating = request.form['movieRating']

    rating_list = ['1', '2', '3' ,'4', '5']

    if not (title == None or title == '') and not (director == None or director == ''):
        for rating_check in rating_list:
            if rating == rating_check:
                break
        else:
            return redirect(f'/movies/new')

    movie_repository.create_movie(title, director, rating)
    return redirect(url_for('list_all_movies'))


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # Grade Feature 4 for Jason Khotsombath
    current_movie = movie_repository.get_movie_by_id(movie_id)

    return render_template('get_single_movie.html', current_movie=current_movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    current_movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('edit_movies_form.html', current_movie=current_movie)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # Jason Khotsombath accidently did feature 5
    title = request.form.get('title')
    director = request.form.get('director')
    rating = request.form.get('rating')
    rating_list = ['1', '2', '3' ,'4', '5']

    if not (title == None or title == '') and not (director == None or director == ''):
        for rating_check in rating_list:
            if rating == rating_check:
                break
        else:
            return redirect(f'/movies/{movie_id}/edit')

    # After updating the movie in the database, we redirect back to that single movie page
        movie_repository.update_movie(movie_id, title, director, rating)
        return redirect(f'/movies/{movie_id}')
    else:
        return redirect(f'/movies/{movie_id}/edit')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    # Jason Khotsombath accidently did feature 6
    if movie_id not in [movie.movie_id for _, movie in movie_repository.get_all_movies().items()]:
        abort(400)
        
    movie_repository.delete_movie(movie_id)
    return redirect('/movies')
