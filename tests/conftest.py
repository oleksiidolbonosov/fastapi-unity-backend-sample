import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_headers(client):
    response = client.post("/api/login", json={"player_id": "test_player"})
    token = response.json()["token"]
    return {"Authorization": f"Bearer {token}"}
