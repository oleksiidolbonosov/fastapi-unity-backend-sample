def test_login_success(client):
    response = client.post("/api/login", json={"player_id": "test_player"})
    assert response.status_code == 200
    assert "token" in response.json()

def test_protected_endpoint_without_token(client):
    response = client.post("/api/sync", json={"player_id": "test", "state": {}})
    assert response.status_code == 401
