# src/routes/pets_routes.py

from fastapi import APIRouter, Request
import httpx
from src.config.config import get_env

router = APIRouter(prefix="/api/pets", tags=["Pets"])

@router.post("/")
async def create_pet(req: Request):
    body = await req.json()
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{get_env('CREATE_PET_URL')}/api/pets/", json=body)
        return response.json()

@router.get("/")
async def get_pets():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{get_env('GET_PET_URL')}/api/pets")
        return response.json()

@router.get("/{pet_id}")
async def get_pet_by_id(pet_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{get_env('GET_PET_URL')}/api/pets/{pet_id}")
        return response.json()

@router.put("/{pet_id}")
async def update_pet(pet_id: str, req: Request):
    body = await req.json()
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{get_env('UPDATE_PET_URL')}/api/pets/{pet_id}", json=body)
        return response.json()

@router.delete("/{pet_id}")
async def delete_pet(pet_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{get_env('DELETE_PET_URL')}/api/pets/{pet_id}")
        return response.json()
