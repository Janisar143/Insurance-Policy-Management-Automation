import requests


def test_create_policy():
    url = "https://api.example.com/policies"
    payload = {"policy_name": "Health Insurance"}
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["message"] == "Policy created successfully"
