from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os

from app.database import get_db

app = FastAPI()


@app.get("/books")
async def get_all_books():
    """
        Retrive all books
    """
    pass


@app.get("/books/{book_id}")
async def get_book_by_id():
    """
        Retrive a book with id
    """
    pass

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
    