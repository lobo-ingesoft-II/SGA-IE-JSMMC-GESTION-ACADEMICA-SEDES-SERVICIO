from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_sede():
    response = client.post("/sedes/", json={
        "nombre": "Sede Principal"
    })
    assert response.status_code == 200
    assert response.json()["nombre"] == "Sede Principal"

def test_get_sede():
    response = client.get("/sedes/1")
    assert response.status_code == 200
    assert "nombre" in response.json()

def test_list_sedes():
    response = client.get("/sedes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)