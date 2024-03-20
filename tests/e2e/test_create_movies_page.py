# TODO: Feature 2
from flask.testing import FlaskClient


def test_home_page(test_app: FlaskClient):
    response = test_app.get('/movies/new')
    response_data = response.data.decode('utf-8')
    

    assert '<h1 class="mb-5">Create Movie Rating</h1>' in response_data
