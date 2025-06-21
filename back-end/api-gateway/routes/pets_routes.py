import os
from dotenv import load_dotenv
from fastapi import APIRouter, Request, HTTPException
import httpx

load_dotenv()

router = APIRouter(prefix="/api/pets", tags=["Pets"])

CREATE_URL = os.getenv("CREATE_PET_URL") + "/api/pets"
GET_URL    = os.getenv("GET_PET_URL") + "/api/pets"
UPDATE_URL = os.getenv("UPDATE_PET_URL") + "/api/pets"
DELETE_URL = os.getenv("DELETE_PET_URL") + "/api/pets"


@router.post("/")
async def create_pet(request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.post(CREATE_URL, json=body)

        return response.json()


@router.get("/")
async def get_all_pets():
    async with httpx.AsyncClient() as client:
        response = await client.get(GET_URL)
        return response.json()


@router.get("/{pet_id}")
async def get_pet_by_id(pet_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{GET_URL}/{pet_id}")
        return response.json()


@router.put("/{pet_id}")
async def update_pet(pet_id: int, request: Request):
    body = await request.json()
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{UPDATE_URL}/{pet_id}", json=body)
        return response.json()


@router.delete("/{pet_id}")
async def delete_pet(pet_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{DELETE_URL}/{pet_id}")
        return response.json()
