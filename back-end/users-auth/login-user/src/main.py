from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import auth_routes

app = FastAPI(
    title="Login User Microservice",
    description="Handles user login and token generation",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "✅ Login User Service is running!"}
