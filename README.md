# Books Fast-API

## Advanced FastAPI Project

This is an advanced REST API built with Python and FastAPI, integrating with MongoDB for CRUD operations (Create, Read, Update, Delete) on books. FastAPI is a powerful web framework for building APIs, while MongoDB is a NoSQL database that provides flexibility and scalability.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/<your-username>/<your-repo-name>
```

Change into the project directory:

```bash
cd <your-repo-name>
```
Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Configure the `.env` file with your own **MongoDB** credentials:

```bash
cp .env.example .env
```

Edit `.env` with your own values:

```ini
MONGO_URI=<your-mongodb-uri>
```

Run the application:

```bash
uvicorn main:app --reload
```

The application will start and be available at http://localhost:8000.

## API Endpoints

Retrieve a list of books:
```http
GET /books
```

Returns a list of all books in the system:

```console
curl http://localhost:8000/books/ -H "Accept: application/json"
```

Retrieve details for a specific book:

```http
GET /books/{book_id}
```

Returns details for a specific book with the given book_id:

```console
curl http://localhost:8000/books/1 -H "Accept: application/json"
```

Add a new book:

```http
POST /books
```

Adds a new book to the system. The request body should include a **JSON** object with the following properties:

- `title` (string, required): the title of the book
- `author` (string, required): the author of the book
- `description` (string): the description of the book
- `published_year` (integer): the published year of the book
- `publisher` (string): the publisher of the book

```console
curl -X POST http://localhost:8000/books/
   -H 'Content-Type: application/json'
   -d '{"title":"The Lord of the Rings", "author": "J.R.R. Tolkien", "published_year": 1954, "publisher": "George Allen & Unwin", "description": "A hobbit named Frodo Baggins and his companions set out on a quest to destroy the One Ring and defeat the dark lord Sauron."}'
```

Update an existing book:

```http
PUT /books/{book_id}
```

Updates an existing book with the given `book_id`. The request body should include a **JSON** object with the following properties:

- `title` (string): the new title for the book
- `author` (string): the new author for the book
- `description` (string): the new description for the book
- `published_year` (integer): the new published year for the book
- `publisher` (string): the new publisher for the book

```console
curl -X PUT http://localhost:8000/books/1
     -H "Accept: application/json"
     -d '{"title": "The Fellowship of the Ring", "author": "J.R.R. Tolkien", "published_year": 1954, "publisher": "George Allen & Unwin", "description": "
```

Copyright 2023, Max Base
