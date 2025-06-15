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

def get_pet_by_id(pet_id: int):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM pets WHERE id = %s;", (pet_id,))
        pet = cur.fetchone()

        cur.close()
        conn.close()

        if pet is None:
            raise HTTPException(status_code=404, detail="Pet not found")

        return pet

    except HTTPException:
        raise  # Permite que el 404 pase tal cual
    except Exception as e:
        print("❌ Error retrieving pet:", e)
        raise HTTPException(status_code=500, detail="Server error retrieving pet")

def get_pets_by_client_id(client_id: int):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM pets WHERE client_id = %s ORDER BY id ASC;", (client_id,))
        pets = cur.fetchall()

        cur.close()
        conn.close()

        return pets

    except Exception as e:
        print("❌ Error retrieving pets by client_id:", e)
        raise HTTPException(status_code=500, detail="Server error retrieving pets by client")


    
    
