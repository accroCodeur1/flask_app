import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_events_api(client):
    response = client.get('/api/events')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_news_api(client):
    response = client.get('/api/news')
    assert response.status_code == 200
    assert isinstance(response.json, list)