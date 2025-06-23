from dotenv import load_dotenv
import os
from pathlib import Path

# Carga las variables del archivo .env ubicado en el root del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

# Configuración del entorno
class Settings:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

settings = Settings()

# Función auxiliar para obtener una variable de entorno específica
def get_env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"❌ Environment variable '{key}' not found.")
    return value
