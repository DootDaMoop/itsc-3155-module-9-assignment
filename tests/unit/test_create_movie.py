# TODO: Feature 2s
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository


def test_create_movie():
    movie_repo = get_movie_repository()
    movie_repo.create_movie('Star Wars', 'George Lucas', 5)
    
    if movie_repo.get_movie_by_title('Star Wars').title == 'Star Wars' and movie_repo.get_movie_by_title('Star Wars').director == 'George Lucas' and movie_repo.get_movie_by_title('Star Wars').rating == 5:
        assert True
    else:
        assert False
