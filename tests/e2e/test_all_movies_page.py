# TODO: Feature 1
from flask.testing import FlaskClient
from src.models.movie import Movie
from src.repositories import movie_repository
movie_repository_var = movie_repository

def test_list_all_movies(test_app: FlaskClient):
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')

    movie_repo = movie_repository_var.get_movie_repository()

    movie_repo.create_movie('Star Wars', 'George Lucas', 5)
    movie_repo.create_movie('Harry Potter', 'Me', 3)
    movie_repo.create_movie('Huh?', 'What?', 1)
    
    assert '<td id="movie_title">Harry Potter</td>' in response_data
    assert '<td id="movie_title">Huh?</td>' in response_data
    assert '<table class="table">' in response_data