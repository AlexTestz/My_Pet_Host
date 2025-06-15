from fastapi import HTTPException
from src.database.database import get_connection

def get_all_pets():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM pets ORDER BY id ASC;")
        pets = cur.fetchall()

        cur.close()
        conn.close()

        return pets

    except Exception as e:
        print("❌ Error al obtener mascotas:", e)
        raise HTTPException(status_code=500, detail="Server error retrieving pets")
