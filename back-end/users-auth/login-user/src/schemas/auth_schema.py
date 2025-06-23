from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    username_or_email: str = Field(..., example="usuario@example.com")
    password: str = Field(..., example="MiContrasena123")

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
