from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

def get_db():
    
    db = client.get_database()
    try:
        yield db
    finally:
        pass
