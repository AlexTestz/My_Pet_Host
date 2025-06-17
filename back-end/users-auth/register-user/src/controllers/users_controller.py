# src/controllers/users_controller.py

from fastapi import HTTPException
from src.schemas.user_schema import UserCreate
from src.database.database import get_connection
import bcrypt
import re

def validate_password_strength(password: str):
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long")
    if not re.search(r"[A-Z]", password):
        raise HTTPException(status_code=400, detail="Password must contain at least one uppercase letter")
    if not re.search(r"[a-z]", password):
        raise HTTPException(status_code=400, detail="Password must contain at least one lowercase letter")
    if not re.search(r"\d", password):
        raise HTTPException(status_code=400, detail="Password must contain at least one number")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise HTTPException(status_code=400, detail="Password must contain at least one special character")

def create_user_in_db(user: UserCreate):
    try:
        conn = get_connection()
        cur = conn.cursor()

        # Verificar si el email o username ya existen
        cur.execute("SELECT id FROM users WHERE email = %s OR username = %s", (user.email, user.username))
        if cur.fetchone():
            raise HTTPException(status_code=409, detail="User with this email or username already exists")

        # ✅ Validar fortaleza de la contraseña
        validate_password_strength(user.password)

        # Hashear la contraseña
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Insertar el usuario
        cur.execute("""
            INSERT INTO users (username, email, password, role)
            VALUES (%s, %s, %s, %s)
            RETURNING id, username, email, role;
        """, (user.username, user.email, hashed_password, user.role))

        new_user = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return new_user

    except HTTPException:
        raise
    except Exception as e:
        print("❌ Error registering user:", e)
        raise HTTPException(status_code=500, detail="Server error while registering user")
