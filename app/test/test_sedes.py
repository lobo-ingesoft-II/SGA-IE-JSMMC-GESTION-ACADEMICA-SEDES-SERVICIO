# app/test/test_sedes.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import init_db, engine, Base
from sqlalchemy.orm import Session

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Crear tablas en una base limpia para tests
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    # Opcional: limpiar tras tests
    Base.metadata.drop_all(bind=engine)

def test_create_sede():
    response = client.post("/sedes/", json={"nombre": "Sede Test"})
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Sede Test"
    assert "id_sede" in data

def test_get_sede():
    # Asumimos que la primera sede tiene ID=1
    response = client.get("/sedes/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id_sede"] == 1
    assert data["nombre"] == "Sede Test"

def test_list_sedes():
    response = client.get("/sedes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(s["id_sede"] == 1 for s in data)

def test_update_sede():
    response = client.put("/sedes/1", json={"nombre": "Sede Test Actualizada"})
    assert response.status_code == 200
    data = response.json()
    assert data["id_sede"] == 1
    assert data["nombre"] == "Sede Test Actualizada"

def test_delete_sede():
    response = client.delete("/sedes/1")
    assert response.status_code == 204
    # Comprobar que ya no existe
    get_resp = client.get("/sedes/1")
    assert get_resp.status_code == 404

def test_list_empty_after_delete():
    response = client.get("/sedes/")
    assert response.status_code == 200
    assert response.json() == []
