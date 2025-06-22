# src/routes/users_routes.py

from fastapi import APIRouter
from src.schemas.user_schema import UserCreate
from src.controllers.users_controller import create_user_in_db

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.post("/register", summary="Register a new user")
def register_user(user: UserCreate):
    new_user = create_user_in_db(user)
    return {
        "message": "✅ User registered successfully",
        "user": new_user
    }
