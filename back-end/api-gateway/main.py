from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import pets_routes, clients_routes

app = FastAPI(title="🐶 API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers por dominio
app.include_router(pets_routes.router)
app.include_router(clients_routes.router)

@app.get("/")
def root():
    return {"message": "🧭 API Gateway is running!"}
