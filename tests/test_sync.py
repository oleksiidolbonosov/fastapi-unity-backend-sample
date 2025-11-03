def test_sync_with_token(client, auth_headers):
    payload = {"player_id":"test_player","state":{}}
    response = client.post("/api/sync", json=payload, headers=auth_headers)
    assert response.status_code == 200
    assert response.json().get("ok") is True
