from fastapi import APIRouter, Request
import httpx
from src.config.config import get_env

router = APIRouter(prefix="/api/users")

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
async def change_password(req: Request):
    async with httpx.AsyncClient() as client:
        body = await req.json()
        token = req.headers.get("Authorization")
        headers = {"Authorization": token} if token else {}
        response = await client.put(f"{get_env('CHANGE_PASSWORD_URL')}/api/users/change-password", json=body, headers=headers)
        return response.json()
