def test_create_user(client):
    data={"title": "test", "content": "test"}
    response=client.post("/blogs/",json=data)
    assert response.status_code==201
    assert response.json()["title"]=="test"
    
    
    
# def test_get_user(client):
#     response=client.get("/blogs/1")
#     assert response.status_code==200
#     assert response.json()["id"]==1