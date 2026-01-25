from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")  # ❗ NO localhost fallback
DATABASE_NAME = os.getenv("DATABASE_NAME", "scholarship_finder")

if not MONGO_URI:
    raise RuntimeError("❌ MONGO_URI environment variable not set")

client = None
database = None

async def connect_to_mongo():
    global client, database
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        database = client[DATABASE_NAME]

        # Test connection
        await client.admin.command("ping")
        print("✅ Connected to MongoDB Atlas")
    except ServerSelectionTimeoutError as e:
        print("❌ Failed to connect to MongoDB", e)
        raise

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("✅ MongoDB connection closed")

def get_database():
    return database
