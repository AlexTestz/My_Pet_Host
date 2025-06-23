# src/routes/auth_routes.py

from fastapi import APIRouter
from src.schemas.auth_schema import LoginRequest
from src.controllers.auth_controller import login_user

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/login")
def login(credentials: LoginRequest):
    return login_user(credentials)
