import pytest
from httpx import AsyncClient
from baldussi_backend.main import app
from baldussi_backend.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from baldussi_backend.models import Base
from fastapi.testclient import TestClient

# --- Configuração do banco em memória para os testes ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
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

def test_create_user():
    with TestClient(app) as client:
        response = client.post(
            "/users/register",
            json={"username": "teste", "password": "1234", "is_admin": True }
        )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "teste"
    assert "id" in data
