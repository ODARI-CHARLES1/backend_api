import hashlib
from typing import Optional, List
from Models.user_model import UserCreate, UserUpdate, UserResponse

class UserService:
    def __init__(self, repository):
        self.repository = repository

    async def get_all_users(self, skip: int = 0, limit: int = 100) -> List[UserResponse]:
        users = await self.repository.get_all(skip, limit)
        return [UserResponse(**user) for user in users]

    async def get_user_by_id(self, user_id: str) -> Optional[UserResponse]:
        user = await self.repository.get_by_id(user_id)
        return UserResponse(**user) if user else None

    async def create_user(self, user: UserCreate) -> UserResponse:
        existing = await self.repository.get_by_email(user.email)
        if existing:
            raise ValueError("Email already exists")
        
        user_dict = user.model_dump()
        user_dict["hashed_password"] = self._hash_password(user_dict.pop("password"))
        created = await self.repository.create(user_dict)
        return UserResponse(**created)

    async def update_user(self, user_id: str, user: UserUpdate) -> bool:
        update_data = user.model_dump(exclude_unset=True)
        if "password" in update_data:
            update_data["hashed_password"] = self._hash_password(update_data.pop("password"))
        return await self.repository.update(user_id, update_data)

    async def delete_user(self, user_id: str) -> bool:
        return await self.repository.delete(user_id)

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self._hash_password(plain_password) == hashed_password