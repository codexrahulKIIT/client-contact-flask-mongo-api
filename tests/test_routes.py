import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_clients():
    response = requests.get(f"{BASE_URL}/clients")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_client():
    new_client = {
        "name": "Test User",
        "email": "testuser@example.com",
        "company": "Test Corp",
        "phone": "1234567890",
        "status": "Active"
    }
    response = requests.post(f"{BASE_URL}/clients", json=new_client)
    assert response.status_code == 201
    data = response.json()
    assert "inserted_id" in data

def test_invalid_post_data():
    incomplete_data = {
        "name": "No Email"
    }
    response = requests.post(f"{BASE_URL}/clients", json=incomplete_data)
    assert response.status_code == 400  # Adjust based on how you handle validation
