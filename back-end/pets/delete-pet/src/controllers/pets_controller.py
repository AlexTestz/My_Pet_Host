from fastapi import HTTPException
from src.database.database import get_connection

def delete_pet_by_id(pet_id: int):
    try:
        conn = get_connection()
        cur = conn.cursor()

        # Verificar si la mascota existe
        cur.execute("SELECT id FROM pets WHERE id = %s", (pet_id,))
        if cur.fetchone() is None:
            raise HTTPException(status_code=404, detail="Pet not found")

        # Eliminar la mascota
        cur.execute("DELETE FROM pets WHERE id = %s", (pet_id,))
        conn.commit()

        cur.close()
        conn.close()

        return {"message": f"✅ Pet with ID {pet_id} deleted successfully"}

    except HTTPException as e:
        raise e
    except Exception as e:
        print("❌ Error deleting pet:", e)
        raise HTTPException(status_code=500, detail="Server error while deleting pet")
