# src/routes/users_routes.py

from fastapi import APIRouter, Depends, Request
import httpx
from src.config.config import get_env
from src.schemas.user_schema import ChangePasswordRequest
from src.controllers.users_controller import change_password
from src.dependencies import get_current_user  # ⚠️ Este archivo se muestra abajo

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.post("/register")
async def register_user(req: Request):
    async with httpx.AsyncClient() as client:
        body = await req.json()
        response = await client.post(f"{get_env('REGISTER_USER_URL')}/api/users/register", json=body)
        return response.json()

@router.post("/login")
async def login_user(req: Request):
    async with httpx.AsyncClient() as client:
        body = await req.json()
        response = await client.post(f"{get_env('LOGIN_USER_URL')}/api/auth/login", json=body)
        return response.json()

@router.get("/validate-token")
async def validate_token(req: Request):
    token = req.headers.get("Authorization")
    if not token:
        return {"detail": "Authorization header missing"}
    
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": token}
        response = await client.get(f"{get_env('VALIDATE_TOKEN_URL')}/api/auth/validate-token", headers=headers)
        return response.json()

@router.put("/change-password")
def change_password_route(
    data: ChangePasswordRequest,
    user=Depends(get_current_user)
):
    return change_password(user["id"], data)
