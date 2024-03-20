# TODO: Feature 5
from flask.testing import FlaskClient
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

def test_edit_movie_page(test_app: FlaskClient):
    movie_repository = get_movie_repository()
    movie = Movie(27538, 'Dang Folly', 'Pam Galena', 4)
    movie_repository._db.update({movie.movie_id:movie})

    response = test_app.get(f'/movies/{movie.movie_id}/edit')
    response_data = response.data.decode('utf-8')

    assert '<h1>Editing Dang Folly</h1>' in response_data

def test_edit_movie_page_is_invalid(test_app: FlaskClient):
    response = test_app.get(f'/movies/12345/edit')
    response_data = response.data.decode('utf-8')

    assert '<h1 class="mt-5 text-center">Invalid Movie ID</h1>' in response_data