from fastapi import APIRouter, Request, status
import httpx
from utils.jwt_validator import verify_token
import os
from dotenv import load_dotenv

load_dotenv()  # Carga el archivo .env

router = APIRouter(prefix="/api/clients", tags=["Clients"])

CREATE_URL = os.getenv("CREATE_CLIENT_URL") + "/api/clients"
GET_URL    = os.getenv("GET_CLIENT_URL") + "/api/clients"
UPDATE_URL = os.getenv("UPDATE_CLIENT_URL") + "/api/clients"
DELETE_URL = os.getenv("DELETE_CLIENT_URL") + "/api/clients"


@router.post("/")
async def create_client(request: Request):
    verify_token(request)
    body = await request.body()
    async with httpx.AsyncClient() as client:
        response = await client.post(CREATE_URL, content=body, headers=request.headers.raw)
    return response.json()


@router.get("/{client_id}")
async def get_client(client_id: str, request: Request):
    verify_token(request)
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{GET_URL}/{client_id}", headers=request.headers.raw)
    return response.json()


@router.put("/{client_id}")
async def update_client(client_id: str, request: Request):
    verify_token(request)
    body = await request.body()
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{UPDATE_URL}/{client_id}", content=body, headers=request.headers.raw)
    return response.json()


@router.delete("/{client_id}")
async def delete_client(client_id: str, request: Request):
    verify_token(request)
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{DELETE_URL}/{client_id}", headers=request.headers.raw)
    return response.json()
