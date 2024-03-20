# TODO: Feature 6
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository


def test_get_movie_by_id():
    movie_repository = get_movie_repository()
    movie = Movie(93762, 'Warlock War', 'Nicholas Smith', 3)
    movie_repository._db.update({movie.movie_id:movie})
    assert movie_repository.get_movie_by_id(93762) == movie
    
    movie_repository.delete_movie(93762)
    assert movie_repository.get_movie_by_id(93762) == None
