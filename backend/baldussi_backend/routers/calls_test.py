import pytest
from baldussi_backend.main import app
from baldussi_backend.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from baldussi_backend.models import Base

from fastapi.testclient import TestClient
from baldussi_backend.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_calls.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def create_user_and_get_token(username="test_calls_user", password="pass1234"):
    # Tenta registrar (se já existir, ignora o erro 400)
    resp = client.post("/users/register", json={
        "username": username,
        "password": password,
        "is_admin": True
    })
    # Aceitamos 200/201 (criado) ou 400 (já existe)
    assert resp.status_code in (200, 201, 400)

    # Faz login (OAuth2 form data)
    login = client.post("/auth/token", data={"username": username, "password": password})
    assert login.status_code == 200, f"login failed: {login.status_code} {login.text}"
    token = login.json().get("access_token")
    assert token, "no access_token returned"
    return token

def test_calls_raw():
    """
    Test that /calls/raw requires auth and returns 200 when authorized.
    """
    token = create_user_and_get_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.get("/calls/raw", headers=headers)

    assert resp.status_code == 200

def test_calls():
    """
    Test that /calls/get requires auth and returns 200 when authorized.
    """
    token = create_user_and_get_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.get("/calls/get", headers=headers)

    assert resp.status_code == 200

def test_kpi():
    """
    Test that /calls/kpi requires auth and returns 200 when authorized.
    """
    token = create_user_and_get_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.get("/calls/kpi", headers=headers)

    assert resp.status_code == 200

def test_calls_per_day():
    """
    Test that /calls/calls_per_day requires auth and returns 200 when authorized.
    """
    token = create_user_and_get_token()
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.get("/calls/calls_per_day", headers=headers)

    assert resp.status_code == 200
