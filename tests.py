from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_webhook():
    response = client.post("/webhook", json={"key": "value"})
    assert response.status_code == 200

def test_get_data():
    response = client.get("/data")
    assert response.status_code == 200

def test_sync():
    response = client.get("/sync/crm")
    assert response.status_code == 200
