from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.pets_routes import router  # Ajusta el import según tu estructura

app = FastAPI(
    title="Update Pet Microservice",
    description="Microservice to update pets",
    version="1.0.0"
)

# Middleware CORS (si usas frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(router)

@app.get("/")
def root():
    return {"message": "✅ Update Pet Service is running!"}
