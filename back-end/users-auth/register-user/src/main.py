# src/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import users_routes

app = FastAPI(
    title="Register User Microservice",
    description="Microservice for user registration",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(users_routes.router)

# Health Check
@app.get("/")
def root():
    return {"message": "✅ Register User Service is running!"}
