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
        if not all(key in book for key in self.fields):
            return self.unproessable()
        
        response = None
        try:
            response = self.db.books.insert_one(book)
        except Exception:
            return self.error_insert()
        return {
            "detail": "book created successfuly.",
        }
    
    
    def update_book(self, book_id: str , book):
        data = {}
        if "title" in book:
            data["title"] = book["title"]
        if "description" in book:
            data["description"] = book["description"]
        if "author" in book:
            data["author"] = book["author"]
        if "published_year" in book:
            data["published_year"] = book["published_year"]
        if "publisher" in book:
            data["publisher"] = book["publisher"]
        
        try:
            result = self.db.books.update_one({"_id": ObjectId(book_id)}, {"$set": data})
        except Exception as e:
            return self.error_insert()
        
        if result.modified_count > 0:
            return {
                "detail": "book info updated successfuly."
            }
        return self.not_found()
    
    
    def delete_book(self, book_id: str):
        result = self.db.books.delete_one({"_id": ObjectId(book_id)})
        
        if result.deleted_count != 0:
            return {
                "detail": "Book deleted successfully"
            }
        
        return self.not_found()

    
    
    def not_found(self):
        return JSONResponse({
            "detail": "book not found."
        }, 404)
        
    
    def error_insert(self):
        return JSONResponse({
            "detail": "error in insert and update"
        }, 409)
        

    def unproessable(self):
        return JSONResponse({
            "detail": "Missing required keys in request data"
        }, 422)
    
    
    
