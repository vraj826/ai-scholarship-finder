from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "scholarship_finder")

client = None
database = None

async def connect_to_mongo():
    global client, database
    try:
        client = AsyncIOMotorClient(MONGODB_URL)
        database = client[DATABASE_NAME]
        # Test connection
        await client.admin.command('ping')
        print("✅ Connected to MongoDB")
    except ServerSelectionTimeoutError:
        print("❌ Failed to connect to MongoDB")
        raise

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("✅ MongoDB connection closed")

def get_database():
    return database