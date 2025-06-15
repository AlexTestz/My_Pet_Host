from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import pets_routes

app = FastAPI(
    title="Delete Pet Microservice",
    description="Microservice to delete pet records",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pets_routes.router)

@app.get("/")
def root():
    return {"message": "✅ Delete Pet Service is running!"}
# This is the main entry point for the Delete Pet microservice.