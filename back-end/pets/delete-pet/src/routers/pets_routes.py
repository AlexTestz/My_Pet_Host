from fastapi import APIRouter
from src.controllers.pets_controller import delete_pet_by_id

router = APIRouter(prefix="/api/pets", tags=["Pets"])

@router.delete("/{pet_id}")
def delete_pet(pet_id: int):
    return delete_pet_by_id(pet_id)
# This endpoint allows you to delete a pet by its ID.