from fastapi.testclient import TestClient
from baldussi_backend.main import app

def test_calls_raw():
    """
    Test calls raw
    """
    client = TestClient(app)
    response = client.get('/calls/raw')

    assert not response.is_error

def test_calls():
    """
    Test calls
    """

    client = TestClient(app)
    response = client.get('/calls/get')

    assert not response.is_error