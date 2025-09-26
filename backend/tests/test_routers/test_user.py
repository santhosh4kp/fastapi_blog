def test_create_user(client):
    data={"email": "ping@fast.com", "password": "admin123"}
    response=client.post("/users/",json=data)
    assert response.status_code==201
    assert response.json()["email"]=="ping@fast.com"