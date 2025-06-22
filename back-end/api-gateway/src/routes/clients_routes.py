# src/routes/clients_routes.py

from fastapi import APIRouter, Request
import httpx
from src.config.config import get_env

router = APIRouter(prefix="/api/clients", tags=["Clients"])

@router.post("/")
async def create_client(req: Request):
    async with httpx.AsyncClient() as client:
        body = await req.json()
        response = await client.post(f"{get_env('CREATE_CLIENT_URL')}/api/clients", json=body)
        return response.json()

@router.get("/")
async def get_clients():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{get_env('GET_CLIENT_URL')}/api/clients")
        return response.json()

@router.put("/{client_id}")
async def update_client(client_id: str, req: Request):
    async with httpx.AsyncClient() as client:
        body = await req.json()
        response = await client.put(f"{get_env('UPDATE_CLIENT_URL')}/api/clients/{client_id}", json=body)
        return response.json()
    
@router.get("/{client_id}")
async def get_client_by_id(client_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{get_env('GET_CLIENT_URL')}/api/clients/{client_id}")
        return response.json()


@router.delete("/{client_id}")
async def delete_client(client_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{get_env('DELETE_CLIENT_URL')}/api/clients/{client_id}")
        return response.json()
