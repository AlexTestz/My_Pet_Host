from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.users_routes import router
from src.routes.clients_routes import router as clients_router
from src.routes import pets_routes


app = FastAPI(title="API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)
app.include_router(clients_router)
app.include_router(pets_routes.router)



@app.get("/")
def root():
    return {"message": "✅ API Gateway running"}
