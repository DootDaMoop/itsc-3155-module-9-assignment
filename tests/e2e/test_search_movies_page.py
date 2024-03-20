# TODO: Feature 3
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

def test_search_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data.decode('utf-8')

    assert '<h1 class="mb-5">Search Movie Ratings</h1>' in response_data

def test_search_page_movie_found(test_app: FlaskClient):
    
    test_repository = get_movie_repository()
    test_movie = test_repository.create_movie('Family Guy', 'Gege Akutami', 5) # Movie to test 

    response = test_app.get(f'/movies/search?search={test_movie.title}')
    response_data = response.data.decode('utf-8')

    assert f'<h6 class="mx-3">Movie: {test_movie.title}</p>' in response_data
    


