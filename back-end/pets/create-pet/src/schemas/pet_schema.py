from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import date


class PetCreate(BaseModel):
    name: constr(min_length=2) = Field(..., example="Firulais")
    species: constr(min_length=3) = Field(..., example="Dog")
    breed: Optional[str] = Field(None, example="Labrador")
    age: Optional[int] = Field(None, gt=0, example=3)
    admission_date: date = Field(..., example="2025-06-12")
    notes: Optional[str] = Field(None, example="Friendly with other pets")
    client_id: int = Field(..., example=1)
