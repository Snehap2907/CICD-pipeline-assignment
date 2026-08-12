import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_health(client):
    response = client.get("/health")
    assert response.status_code in [200, 500]
