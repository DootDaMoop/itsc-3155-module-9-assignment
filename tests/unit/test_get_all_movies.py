# TODO: Feature 1
from src.models.movie import Movie
from src.repositories import movie_repository

def test_get_all_movies():
    movie_repo = movie_repository.get_movie_repository()
    movie_repo.create_movie('Star Wars', 'George Lucas', 5)
    movie_repo.create_movie('Harry Potter', 'Me', 3)
    movie_repo.create_movie('Huh?', 'What?', 1)

    movie1 = movie_repo.get_movie_by_title('Star Wars')
    movie2 = movie_repo.get_movie_by_title('Harry Potter')
    movie3 = movie_repo.get_movie_by_title('Huh?')
    movie_dict = movie_repo.get_all_movies()
    
    if movie1 and movie2 and movie3 in movie_dict:
        assert True