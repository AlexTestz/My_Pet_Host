from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import date

# ✅ Para entrada de datos (PUT / PATCH)
class PetUpdate(BaseModel):
    name: Optional[constr(min_length=2)] = Field(None, example="Firulais")
    species: Optional[constr(min_length=3)] = Field(None, example="Dog")
    breed: Optional[str] = Field(None, example="Labrador")
    age: Optional[int] = Field(None, gt=0, example=3)
    admission_date: Optional[date] = Field(None, example="2025-06-12")
    notes: Optional[str] = Field(None, example="Very friendly")
    client_id: Optional[int] = Field(None, example=1)

# ✅ Para respuestas (después de actualizar)
class Pet(BaseModel):
    id: int
    name: str
    species: str
    breed: Optional[str]
    age: Optional[int]
    admission_date: date
    notes: Optional[str]
    client_id: int

    class Config:
        orm_mode = True
