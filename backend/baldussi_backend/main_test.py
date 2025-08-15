from fastapi.testclient import TestClient
from baldussi_backend.main import app

def test_ping_should_be_pong():
    """
    Test ping
    """
    client = TestClient(app)
    response = client.get('/ping')

    assert response.json() == {"status": "pong"}
