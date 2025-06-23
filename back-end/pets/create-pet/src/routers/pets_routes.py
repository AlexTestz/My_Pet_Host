from fastapi import APIRouter
from src.schemas.pet_schema import PetCreate
from src.controllers.pets_controller import create_pet_in_db

router = APIRouter(prefix="/api/pets", tags=["Pets"])


@router.post("/")
def create_pet(pet: PetCreate):
    new_pet = create_pet_in_db(pet)
    return {
        "message": "Pet registered successfully ✅",
        "pet": new_pet
    }
