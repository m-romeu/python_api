from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthz(test_app):
    response = test_app.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"healthz": "ok"}