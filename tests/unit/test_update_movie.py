# TODO: Feature 5
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository


def test_update_movie():
    movie_repository = get_movie_repository()
    movie = Movie(72539, 'Flapjacks', 'Lincoln Paul', 4)
    movie_repository._db.update({movie.movie_id:movie})
    assert movie_repository.get_movie_by_id(72539).title == 'Flapjacks'
    assert movie_repository.get_movie_by_id(72539).director == 'Lincoln Paul'
    assert movie_repository.get_movie_by_id(72539).rating == 4

    movie_repository.update_movie(72539, 'Software Engineering 101', 'Jacob Krevat', 5)
    assert movie_repository.get_movie_by_id(72539).title == 'Software Engineering 101'
    assert movie_repository.get_movie_by_id(72539).director == 'Jacob Krevat'
    assert movie_repository.get_movie_by_id(72539).rating == 5
