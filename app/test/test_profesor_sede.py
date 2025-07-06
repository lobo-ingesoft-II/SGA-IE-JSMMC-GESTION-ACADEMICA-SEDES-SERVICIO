import pytest
import requests
from fastapi.testclient import TestClient
from app.main import app
from app.db import Base, engine

client = TestClient(app)

# Dummy response para simular auth_api
class DummyResponse:
    def __init__(self, status_code):
        self.status_code = status_code

@pytest.fixture(autouse=True)
def mock_auth(monkeypatch):
    def fake_get(url):
        # Todas las llamadas a auth_api devuelven 200 OK
        return DummyResponse(200)
    monkeypatch.setattr(requests, "get", fake_get)
    yield

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Levanta BD limpia
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_assign_and_list_by_profesor():
    # 1) Creamos una sede
    resp = client.post("/sedes/", json={"nombre": "Sede Test"})
    assert resp.status_code == 200
    sede_id = resp.json()["id_sede"]

    # 2) Asignamos el profesor #1 a esa sede
    resp2 = client.post("/sedes/profesor_sede/", json={
        "id_profesor": 1,
        "id_sede": sede_id
    })
    assert resp2.status_code == 200
    data = resp2.json()
    assert data["id_profesor"] == 1
    assert data["id_sede"] == sede_id
    assert "id_profesor_sede" in data

    # 3) Consultamos sedes por profesor
    resp3 = client.get(f"/sedes/por_profesor/1")
    assert resp3.status_code == 200
    listado = resp3.json()
    assert isinstance(listado, list)
    assert any(s["id_sede"] == sede_id for s in listado)

def test_sedes_por_profesor_sin_asignaciones():
    # Usamos el mismo mock_auth que devuelve 200, pero no hay asignaciones para el profesor 999
    resp = client.get("/sedes/por_profesor/999")
    assert resp.status_code == 200
    assert resp.json() == []
