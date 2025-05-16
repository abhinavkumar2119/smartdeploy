import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"SmartDeploy App Running!" in response.data


def test_add(client):
    response = client.post('/add', json={'a': 2, 'b': 3})
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['result'] == 5


def test_ping(client):
    response = client.get('/ping')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['status'] == 'ok'
