# src/schemas/user_schema.py

from pydantic import BaseModel, Field, constr

class ChangePasswordRequest(BaseModel):
    old_password: str = Field(..., example="oldpassword123")
    new_password: constr(min_length=8) = Field(..., example="newStrongPassword2024")
