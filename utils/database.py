from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

mongo_client = AsyncIOMotorClient(Config.DATABASE_URL)
db = mongo_client[Config.DATABASE_NAME]
users = db.users

async def add_user(user_id, name):
    await users.update_one(
        {"user_id": user_id},
        {"$set": {"name": name}},
        upsert=True
    )

async def get_user_count():
    return await users.count_documents({})
