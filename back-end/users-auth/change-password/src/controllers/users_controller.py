# src/controllers/users_controller.py

from fastapi import HTTPException
from src.database.database import get_connection
from src.schemas.user_schema import ChangePasswordRequest
import bcrypt

def change_password(data: ChangePasswordRequest):
    try:
        conn = get_connection()
        cur = conn.cursor()

        # 1️⃣ Verificar si el usuario existe
        cur.execute("SELECT password FROM users WHERE id = %s", (data.user_id,))
        result = cur.fetchone()
        if not result:
            raise HTTPException(status_code=404, detail="User not found")

        stored_password = result['password']

        # 2️⃣ Verificar contraseña antigua
        if not bcrypt.checkpw(data.old_password.encode('utf-8'), stored_password.encode('utf-8')):
            raise HTTPException(status_code=401, detail="Old password is incorrect")

        # 3️⃣ Hashear nueva contraseña
        new_hashed = bcrypt.hashpw(data.new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # 4️⃣ Actualizar la contraseña
        cur.execute("UPDATE users SET password = %s WHERE id = %s", (new_hashed, data.user_id))
        conn.commit()

        cur.close()
        conn.close()

        return {"message": "✅ Password updated successfully"}

    except HTTPException:
        raise
    except Exception as e:
        print("❌ Error changing password:", e)
        raise HTTPException(status_code=500, detail="Server error while changing password")
