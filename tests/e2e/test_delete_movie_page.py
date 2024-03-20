# TODO: Feature 6
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_delete_movie_page(test_app: FlaskClient):
    test_movie_repository = get_movie_repository()
    length = len(test_movie_repository.get_all_movies())

    movie = test_movie_repository.create_movie('Termination', 'Joe Jugan', 2)

    response = test_app.post(f'/movies/{movie.movie_id}/delete')
    assert length == len(test_movie_repository.get_all_movies())

def test_delete_movie_page_is_invalid(test_app: FlaskClient):
    # Random Movie id
    movie_id = 82634
    response = test_app.post(f'/movies/{movie_id}/delete')
    assert response.status_code == 400