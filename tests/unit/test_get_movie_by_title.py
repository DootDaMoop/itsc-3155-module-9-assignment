# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository 


def test_get_movie_by_title():
    test_repository = get_movie_repository()
    movie = test_repository.create_movie("Rush Hour", "Brock Obama", 10)
    assert test_repository.get_movie_by_title("Rush Hour") == movie
    assert test_repository.get_movie_by_title("Rush Hour").rating == movie.rating
    assert test_repository.get_movie_by_title("Rush Hour").director == movie.director