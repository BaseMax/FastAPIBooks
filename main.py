from fastapi import FastAPI, HTTPException, Depends
from pymongo import MongoClient
import os

from app.database import get_db
from app.book import Book

app = FastAPI()


@app.get("/books")
async def get_all_books(db = Depends(get_db)):
    """
        Retrive all books
    """
    book_instance = Book(db)
    return book_instance.get_all_books()


@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int, db = Depends(get_db)):
    """
        Retrive a book with id
    """
    book_instance = Book(db)
    return book_instance.get_book_by_id(book_id)


@app.post("/books")
async def add_a_new_book():
    """
        Create a new book
    """
    pass


@app.put("/books/{book_id}")
async def edit_book_by_id():
    """
        Edit a book
    """
    pass


@app.delete("/books/{book_id}")
async def delete_a_book():
    """
        Delete a book by id
    """
    pass
