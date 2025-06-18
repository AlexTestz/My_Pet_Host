# src/routes/users_routes.py

from fastapi import APIRouter
from src.schemas.user_schema import ChangePasswordRequest
from src.controllers.users_controller import change_password

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.put("/change-password")
def change_password_route(data: ChangePasswordRequest):
    return change_password(data)
