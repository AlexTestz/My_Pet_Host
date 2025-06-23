from fastapi import APIRouter, Path, Body
from src.schemas.pet_schema import PetUpdate
from src.controllers.pets_controller import update_pet_in_db

router = APIRouter(
    prefix="/api",
    tags=["Pets"]
)

@router.put("/pets/{pet_id}")
def update_pet(
    pet_id: int = Path(..., description="ID of the pet to update"),
    pet_data: PetUpdate = Body(...)
):

    updated_pet = update_pet_in_db(pet_id, pet_data)
    return {
        "message": "✅ Pet updated successfully",
        "pet": updated_pet
    }
