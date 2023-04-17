from fastapi import Depends
from fastapi.responses import JSONResponse

from .database import get_db
class Book:
    """
        CRUD operations in books in database
    """
    def __init__(self, db = Depends(get_db)) -> None:
        self.db = db
        
        
    def get_book_by_id(self, id: int):
        book = self.db.books.find_one({
            "id": id
        })
        if not book:
            return self.not_found()
        return book
    
    
    def get_all_books(self):
        books = []
        for book in self.db.books.find():
            books.append(book)
        return books
        
        
    def not_found(self):
        return JSONResponse({
            "detail": "book not found."
        }, 404)
