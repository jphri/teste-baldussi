import pytest
from httpx import AsyncClient
from baldussi_backend.main import app
from baldussi_backend.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from baldussi_backend.models import Base

from fastapi.testclient import TestClient
from baldussi_backend.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_auth.db"
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


def test_login_success():
    with TestClient(app) as ac:
        ac.post("/users/register", json={"username": "authuser", "password": "12345"})
        response = ac.post(
            "/auth/token",
            data={"username": "authuser", "password": "12345"}  # OAuth2 usa form-data
        )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"].lower() == "bearer"

def test_login_fail_wrong_password():
    with TestClient(app) as ac:
        response = ac.post(
            "/auth/token",
            data={"username": "authuser", "password": "wrongpass"}
        )

    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"