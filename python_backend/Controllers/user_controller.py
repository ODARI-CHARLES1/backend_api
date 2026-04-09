from fastapi import HTTPException, status
from typing import List
from Models.user_model import UserCreate, UserUpdate, UserResponse
from Services.user_service import UserService

class UserController:
    def __init__(self, service: UserService):
        self.service = service

    async def get_users(self, skip: int = 0, limit: int = 100) -> List[UserResponse]:
        return await self.service.get_all_users(skip, limit)

    async def get_user(self, user_id: str) -> UserResponse:
        user = await self.service.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return user

    async def create_user(self, user: UserCreate) -> UserResponse:
        try:
            return await self.service.create_user(user)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )

    async def update_user(self, user_id: str, user: UserUpdate) -> dict:
        updated = await self.service.update_user(user_id, user)
        if not updated:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return {"message": "User updated successfully"}

    async def delete_user(self, user_id: str) -> dict:
        deleted = await self.service.delete_user(user_id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return {"message": "User deleted successfully"}