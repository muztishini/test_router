from fastapi.testclient import TestClient
from main import app
from database import User, SessionLocal
from typing import List, Dict

client = TestClient(app)


def last_user_id():
    db = SessionLocal()
    user = db.query(User).order_by(User.id.desc()).first()
    user_id = user.id if user else None
    return user_id


def test_read_user():
    response = client.get("/users/4/")
    assert response.status_code == 200
    assert response.json() == {
        "id": 4,
        "name": "ddd",
        "age": 444
    }


def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), List)


def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "sss", "age": 11},
    )
    assert response.status_code == 200
    assert isinstance(response.json(), Dict)


def test_update_user():
    response = client.put(
        f"/users/{last_user_id()}/",
        json={"name": "oooo", "age": 3333},
    )
    assert response.status_code == 200
    assert isinstance(response.json(), Dict)


def test_delete_user():
    response = client.delete(f"/users/{last_user_id()}")
    assert response.status_code == 200
