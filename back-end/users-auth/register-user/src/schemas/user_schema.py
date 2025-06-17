# src/schemas/user_schema.py

from pydantic import BaseModel, EmailStr, Field, constr
from typing import Optional

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=50) = Field(..., example="johndoe")
    email: EmailStr = Field(..., example="johndoe@example.com")
    password: constr(min_length=6) = Field(..., example="securePassword123")
    role: Optional[str] = Field("usuario", example="admin")