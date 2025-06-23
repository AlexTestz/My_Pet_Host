from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import validate_routes

app = FastAPI(
    title="Validate Token Microservice",
    description="Validates JWT tokens issued by login-user",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(validate_routes.router)

@app.get("/")
def root():
    return {"message": "✅ Validate Token Service is running!"}
