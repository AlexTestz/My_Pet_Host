# src/routes/services_routes.py

from fastapi import APIRouter, Request
import httpx
from src.config.config import get_env

router = APIRouter(prefix="/api/services", tags=["Services"])

@router.post("/")
async def create_service(req: Request):
    body = await req.json()
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{get_env('CREATE_SERVICE_URL')}/api/services", json=body)
        return response.json()

@router.get("/")
async def get_services():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{get_env('GET_SERVICES_URL')}/api/services")
        return response.json()

@router.get("/{service_id}")
async def get_service_by_id(service_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{get_env('GET_SERVICES_URL')}/api/services/{service_id}")
        
        if response.status_code == 404:
            return {"detail": "Service not found"}
        elif response.status_code != 200:
            return {"detail": f"Unexpected error from service provider (status {response.status_code})"}

        try:
            return response.json()
        except Exception:
            return {"detail": "Response is not valid JSON"}

@router.put("/{service_id}")
async def update_service(service_id: str, req: Request):
    body = await req.json()
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{get_env('UPDATE_SERVICE_URL')}/api/services/{service_id}", json=body)
        return response.json()

@router.delete("/{service_id}")
async def delete_service(service_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{get_env('DELETE_SERVICE_URL')}/api/services/{service_id}")
        return response.json()
