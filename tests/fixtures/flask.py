import pytest

from main import app

@pytest.fixture()
def flask_client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client
