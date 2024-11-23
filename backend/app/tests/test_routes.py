import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_qr_code_not_found():
    response = client.get("/qr_codes/9999")
    assert response.status_code == 404
    assert response.json() == {
        "message": "QR code not found",
        "path": "http://testserver/qr_codes/9999"
    }

def test_create_qr_code():
    response = client.post("/qr_codes/", json={"data": "Sample QR Code"})
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["data"] == "Sample QR Code"
