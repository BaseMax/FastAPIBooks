import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), str)


def test_get_book_by_id():
    response = client.get("/books/643e0c912d32c9fc6c84623b")
    assert response.status_code == 200
    assert isinstance(response.json(), str)
    


def test_add_a_new_book():
    new_book = {
        "title": "Test Book",
        "author": "Test Author",
        "description": "description for book",
        "published_year": 2022,
        "publisher": "Ali Ahmadi"
    }
    response = client.post("/books", json=new_book)
    assert response.status_code == 200
    assert response.json() == {"detail": "book created successfuly."}


def test_edit_book_by_id():
    book_id = "643e0c912d32c9fc6c84623b"
    updated_book = {
        "title": "Updated Test Book23",
        "author": "Updated Test Author",
        "published_year": 2020
    }
    response = client.put(f"/books/{book_id}", json=updated_book)
    assert response.status_code == 200
    assert response.json() == {"detail": "book info updated successfuly."}


def test_book_not_found():
    book_id = "643d59bc25a50004695f4334"
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "book not found."}


def test_unproessable_request():
    data = {}
    response = client.post("/books", json=data)
    assert response.status_code == 422
    assert response.json() == {"detail": "Missing required keys in request data"}


def test_delete_a_book():
    book_id = "643e0c912d32c9fc6c84623b"
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Book deleted successfully"}
