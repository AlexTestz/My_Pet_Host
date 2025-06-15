from fastapi import HTTPException
from src.database.database import get_connection

def delete_pet_by_id(pet_id: int):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM pets WHERE id = %s", (pet_id,))
        pet = cur.fetchone()
        if pet is None:
            raise HTTPException(status_code=404, detail="Pet not found")

        cur.execute("DELETE FROM pets WHERE id = %s", (pet_id,))
        conn.commit()

        cur.close()
        conn.close()

        return {"message": "Pet deleted successfully ✅"}

    except HTTPException:
        raise
    except Exception as e:
        print("❌ Error deleting pet:", e)
        raise HTTPException(status_code=500, detail="Server error while deleting pet")
