def test_get_animals(test_client, auth_headers):
    response = test_client.get("/api/animals", headers=auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_animal(test_client, auth_headers):
    data = {"name": "Lion", "species": "Panthera leo", "age": 5}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 403
    assert response.json["error"] == "Acceso no autorizado para este rol"

def test_get_animal(test_client, auth_headers):
    # Primero crea un animal
    data = {"name": "Tiger", "species": "Panthera tigris", "age": 3}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 403
    assert response.json["error"] == "Acceso no autorizado para este rol"
    animal_id = 1
    # Ahora obtén el animal
    response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers)
    
    assert response.status_code == 404


def test_update_animal(test_client, auth_headers):
    # Primero crea un animal
    data = {"name": "Elephant", "species": "Loxodonta", "age": 10}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 403
    assert response.json["error"] == "Acceso no autorizado para este rol"
    animal_id = 1

    # Ahora actualiza el animal
    update_data = {"name": "Elephant", "species": "Loxodonta africana", "age": 12}
    response = test_client.put(
        f"/api/animals/{animal_id}", json=update_data, headers=auth_headers
    )
    assert response.status_code == 403
    assert response.json["error"] == "Acceso no autorizado para este rol"


def test_delete_animal(test_client, auth_headers):
    # Primero crea un animal
    data = {"name": "Giraffe", "species": "Giraffa camelopardalis", "age": 7}
    response = test_client.post("/api/animals", json=data, headers=auth_headers)
    assert response.status_code == 403
    assert response.json["error"] == "Acceso no autorizado para este rol"
    animal_id = 1

    # Ahora elimina el animal
    response = test_client.delete(f"/api/animals/{animal_id}", headers=auth_headers)
    assert response.status_code == 403
