from fastapi import APIRouter, Depends
from typing import List
from Models.user_model import UserCreate, UserUpdate, UserResponse
from Controllers.user_controller import UserController
from Config.database import get_collection

user_router = APIRouter(prefix="/api/users", tags=["users"])

def get_controller():
    from Services.user_service import UserService
    from Repositories.user_repository import UserRepository
    repository = UserRepository(get_collection("users"))
    service = UserService(repository)
    return UserController(service)

@user_router.get("", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 100, controller: UserController = Depends(get_controller)):
    return await controller.get_users(skip, limit)

@user_router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str, controller: UserController = Depends(get_controller)):
    return await controller.get_user(user_id)

@user_router.post("", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate, controller: UserController = Depends(get_controller)):
    return await controller.create_user(user)

@user_router.put("/{user_id}")
async def update_user(user_id: str, user: UserUpdate, controller: UserController = Depends(get_controller)):
    return await controller.update_user(user_id, user)

@user_router.delete("/{user_id}")
async def delete_user(user_id: str, controller: UserController = Depends(get_controller)):
    return await controller.delete_user(user_id)