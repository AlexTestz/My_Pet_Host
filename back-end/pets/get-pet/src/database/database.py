import psycopg2
from psycopg2.extras import RealDictCursor
from src.config import settings


def get_connection():
    try:
        conn = psycopg2.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            cursor_factory=RealDictCursor  # Resultados como diccionarios
        )
        return conn
    except Exception as e:
        print("❌ Error de conexión a la base de datos:", e)
        raise
