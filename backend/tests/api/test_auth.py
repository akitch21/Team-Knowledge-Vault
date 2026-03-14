def test_get_me(client):
    response = client.get("/auth/me")
    assert response.status_code == 200
    body = response.json()
    assert "id" in body
    assert "username" in body
    assert "email" in body