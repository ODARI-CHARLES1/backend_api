from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    client: AsyncIOMotorClient = None

db = Database()

async def connect_db():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    db.client = AsyncIOMotorClient(mongo_uri)
    return db.client

async def close_db():
    if db.client:
        db.client.close()

def get_database():
    return db.client

def get_collection(name: str):
    return db.client[name]