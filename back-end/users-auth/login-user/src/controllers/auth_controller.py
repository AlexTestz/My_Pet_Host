# src/controllers/auth_controller.py.aasd

from fastapi import HTTPException
from src.database.database import get_connection
from src.schemas.auth_schema import LoginRequest
from src.utils.jwt_manager import create_access_token
import bcrypt

def login_user(credentials: LoginRequest):
    try:
        conn = get_connection()
        cur = conn.cursor()

        # Buscar usuario por email o username
        cur.execute("""
            SELECT id, username, email, password, role 
            FROM users 
            WHERE email = %s OR username = %s
        """, (credentials.username_or_email, credentials.username_or_email))

        user = cur.fetchone()

        if user is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        if not bcrypt.checkpw(credentials.password.encode('utf-8'), user["password"].encode('utf-8')):
            raise HTTPException(status_code=401, detail="Contraseña incorrecta")

        if user["role"] != "admin":
            raise HTTPException(status_code=403, detail="No tienes permiso para iniciar sesión")

        token_data = {
            "sub": str(user["id"]),
            "username": user["username"],
            "email": user["email"],
            "role": user["role"]
        }

        access_token = create_access_token(token_data)

        # ✅ Retornamos también el user_id
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user_id": user["id"]
        }

    except HTTPException:
        raise
    except Exception as e:
        print("❌ Login error:", e)
        raise HTTPException(status_code=500, detail="Error interno en el servidor durante el login")
