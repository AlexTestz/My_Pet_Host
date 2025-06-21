from dotenv import load_dotenv
import os
from pathlib import Path

# Cargar variables del archivo .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")


class Settings:
    PROJECT_NAME: str = "Create Pet Microservice"
    PROJECT_VERSION: str = "1.0.0"
    
    # Base de datos
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    
    # Puerto del microservicio

    PORT: int = int(os.getenv("PORT", 8000))  # usa 8000 si no está definido

settings = Settings()
