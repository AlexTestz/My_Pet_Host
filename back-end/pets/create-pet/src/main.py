from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import pets_routes
from src.config import settings

app = FastAPI(
    title="Create Pet Microservice",
    description="Microservice to register pets in the system",
    version="1.0.0"
)

# CORS middleware (permite que React u otros frontends se conecten)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto luego
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar rutas
app.include_router(pets_routes.router)

# Endpoint raíz (prueba de salud)
@app.get("/")
def health_check():
    return {"message": "✅ Create Pet Service is running!"}
