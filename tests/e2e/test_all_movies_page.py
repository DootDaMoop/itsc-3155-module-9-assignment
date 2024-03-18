# TODO: Feature 1
from flask.testing import FlaskClient
from src.models.movie import Movie

def test_all_movies(test_app: FlaskClient):
    response = test_app.get('/movies')
    response_data = response.data.decode('utf-8')
    movie = Movie(123, 'Star Wars', 'George Lucas', 5)
    
    assert '<td id="movie_title">Star Wars</td>' in response_data