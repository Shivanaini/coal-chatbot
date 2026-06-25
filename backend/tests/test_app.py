import sys
import os

# Allow imports from backend/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_health():
    client = app.test_client()
    response = client.get('/health')

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_chat_reserves():
    client = app.test_client()

    response = client.post(
        '/chat',
        json={"message": "What are coal reserves?"}
    )

    assert response.status_code == 200
    data = response.get_json()
    assert "response" in data
    assert "coal reserves" in data["response"].lower()


def test_chat_unknown():
    client = app.test_client()

    response = client.post(
        '/chat',
        json={"message": "hello chatbot"}
    )

    assert response.status_code == 200
    data = response.get_json()
    assert "I can answer about" in data["response"]