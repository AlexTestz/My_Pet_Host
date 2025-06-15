from fastapi import APIRouter, Query
from src.controllers.pets_controller import get_all_pets, get_pet_by_id, get_pets_by_client_id
from src.schemas.pet_schema import Pet
from typing import List, Optional

router = APIRouter(prefix="/api")

@router.get("/pets", response_model=List[Pet])
def fetch_pets(client_id: Optional[int] = Query(None)):
    if client_id is not None:
        return get_pets_by_client_id(client_id)
    return get_all_pets()

@router.get("/pets/{pet_id}", response_model=Pet)
def fetch_pet_by_id(pet_id: int):
    return get_pet_by_id(pet_id)
