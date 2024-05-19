# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app  # FastAPI 애플리케이션이 정의된 모듈을 import

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
