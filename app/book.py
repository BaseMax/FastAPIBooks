from fastapi import Depends
from fastapi.responses import JSONResponse
import json
from bson import ObjectId


from .database import get_db
class Book:
    """
        CRUD operations in books in database
    """
    fields = [
        "title",
        "author",
        "description",
        "published_year",
        "publisher"
    ]
    
    def __init__(self, db = Depends(get_db)) -> None:
        self.db = db
        
        
    def get_book_by_id(self, id: str):
        book = self.db.books.find_one({
            "_id": ObjectId(id)
        })
        if not book:
            return self.not_found()
        return str(book)
    

    def get_all_books(self):
        books = []
        for book in self.db.books.find():
            books.append(book)
        return str(books)
    
    
    def add_new_book(self, book):
        if not all(key in self.fields for key in book.keys()):
            return self.unproessable()
        
        response = None
        try:
            response = self.db.books.insert_one(book)
        except Exception:
            return self.error_insert()
        return {
            "detail": "book created successfuly.",
        }
    
    
    def not_found(self):
        return JSONResponse({
            "detail": "book not found."
        }, 404)
        
    
    def error_insert(self):
        return JSONResponse({
            "detail": "error in insert"
        }, 409)
        

    def unproessable(self):
        return JSONResponse({
            "detail": "Missing required keys in request data"
        }, 422)
