from pydantic import BaseModel
from typing import Optional
from datetime import date

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
        from_attributes = True

