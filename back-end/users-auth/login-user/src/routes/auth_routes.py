from fastapi import APIRouter
from src.schemas.auth_schema import LoginRequest, TokenResponse
from src.controllers.auth_controller import login_user

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest):
    return login_user(credentials)
