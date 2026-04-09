from bson import ObjectId
from datetime import datetime

class UserRepository:
    def __init__(self, collection):
        self.collection = collection

    async def get_all(self, skip: int = 0, limit: int = 100):
        cursor = self.collection.find().skip(skip).limit(limit)
        users = await cursor.to_list(length=limit)
        return [self._serialize(user) for user in users]

    async def get_by_id(self, user_id: str):
        try:
            user = await self.collection.find_one({"_id": ObjectId(user_id)})
            return self._serialize(user) if user else None
        except Exception:
            return None

    async def get_by_email(self, email: str):
        user = await self.collection.find_one({"email": email})
        return self._serialize(user) if user else None

    async def create(self, user_data: dict):
        user_data["created_at"] = datetime.utcnow()
        user_data["updated_at"] = datetime.utcnow()
        result = await self.collection.insert_one(user_data)
        user_data["id"] = str(result.inserted_id)
        return user_data

    async def update(self, user_id: str, user_data: dict):
        user_data["updated_at"] = datetime.utcnow()
        result = await self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": user_data}
        )
        return result.modified_count > 0

    async def delete(self, user_id: str):
        result = await self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0

    def _serialize(self, document: dict) -> dict:
        if document:
            document["id"] = str(document.pop("_id"))
        return document