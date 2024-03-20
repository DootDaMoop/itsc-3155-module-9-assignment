from flask import Flask, redirect, render_template, request, abort

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()
#movie_repository.create_movie('Software Engineering 101', 'Jacob Krevat', 5)


@app.get('/')
def index():
    # print(movie_repository.get_all_movies())
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
    if movie_id not in [movie.movie_id for _, movie in movie_repository.get_all_movies().items()]:
        abort(400)
    # for movie_id_check in movie_repository._db:
    #     if movie_id_check == movie_id:
    #         break
    #     else:
    #         abort(404)
        
    movie_repository.delete_movie(movie_id)
    return redirect('/movies')
