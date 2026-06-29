import requests

BASE_URL = "http://127.0.0.1:5000"

def test_home():
    r = requests.get(BASE_URL)
    assert r.status_code == 200

def test_send_get():
    r = requests.get(f"{BASE_URL}/send")
    assert r.status_code == 200

def test_send_post():
    r = requests.post(
        f"{BASE_URL}/send",
        json={"message": "pytest"}
    )
    assert r.status_code == 200
    assert r.json()["status"] == "Message sent"