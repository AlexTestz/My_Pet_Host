from fastapi import APIRouter
from src.controllers.pets_controller import get_all_pets
from src.schemas.pet_schema import Pet
from typing import List

router = APIRouter()

@router.get("/pets", response_model=List[Pet])
def fetch_pets():
    return get_all_pets()
