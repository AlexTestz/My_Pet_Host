# 📝 Register User Microservice (users-auth)

Este microservicio permite registrar nuevos usuarios en el sistema de **My Pet Host**. Es responsable de validar, encriptar y almacenar usuarios en la base de datos.

---

## 🚀 Tecnologías

- **Lenguaje:** Python 3.10
- **Framework:** FastAPI
- **Base de datos:** PostgreSQL
- **Hashing:** bcrypt para contraseñas
- **Validación:** Pydantic
- **Docker:** Para despliegue y portabilidad

---

## 📡 Estilo de arquitectura

- **Tipo de API:** RESTful
- **Estilo arquitectónico:** Microservicios
- **Comunicación:** HTTP 
- **Endpoint expuesto:** `/api/users/register` (POST)

---

## 🏗️ Arquitectura interna

- **Patrón de arquitectura:** Separación por capas (n-capas)
  - **Rutas (API Router):** Define los endpoints HTTP
  - **Controladores:** Lógica de negocio y validaciones
  - **Esquemas:** Validación de datos con Pydantic
  - **Base de datos:** Acceso y conexión a PostgreSQL

---

## 🧩 Patrones de diseño aplicados

- **KISS:** Código simple y directo, fácil de mantener.
- **DRY:** Reutilización de lógica y utilidades comunes.
- **SOLID:** Separación de responsabilidades en rutas, controladores y utilidades.
- **YAGNI:** Solo se implementa lo necesario para el registro de usuario.

---

## 🔐 Seguridad

- **Hashing:** Contraseñas almacenadas y comparadas usando bcrypt.
- **Validaciones:** Contraseña fuerte (mínimo 8 caracteres, mayúscula, minúscula, número y carácter especial).
- **CORS:** Configurable con FastAPI Middleware (agregar según necesidad del frontend).

---

## 📦 Estructura del proyecto

```
register-user/
├── src/
│   ├── main.py
│   ├── routes/
│   ├── controllers/
│   ├── schemas/
│   └── database/
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

## ⚙️ Ejecución

**Modo local:**
```bash
python -m venv venv
source venv/bin/activate   # o .\venv\Scripts\activate en Windows
pip install -r requirements.txt
uvicorn src.main:app --reload --port 3006
```

**Docker local:**
```bash
docker build -t register-user .
docker run -p 3006:3006 --env-file .env register-user
```

**DockerHub:**
```bash
docker pull alexmpz/register-user-service:qa
docker run -d -p 3006:3006 --env-file .env alexmpz/register-user-service:qa
```

---

## 🛠️ Endpoint principal

- `POST /api/users/register`

POST http://3.214.168.136:8000/api/users/register

HEADERS     Content-Type      application/json

**Body ejemplo:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "MiContrasena123!",
  "role": "usuario"
}
```

**Validaciones realizadas:**
- Mínimo 8 caracteres
- Al menos una mayúscula
- Al menos una minúscula
- Al menos un número
- Al menos un carácter especial (!@#$...)

**Respuesta Exitosa (201):**
```json
{
  "message": "✅ User registered successfully",
  "user": {
    "id": 7,
    "username": "johndoe",
    "email": "john@example.com",
    "role": "usuario"
  }
}
```

| Código | Motivo                                     |
| ------ | ------------------------------------------ |
| 400    | Contraseña débil                           |
| 409    | Usuario con ese email o username ya existe |
| 422    | Formato inválido en los datos              |
| 500    | Error interno del servidor                 |

**Swagger:**  
http://3.223.253.161:3006/docs

---

## 📚 Notas

- Arquitectura desacoplada, cada microservicio es independiente.
- El patrón n-capas facilita el mantenimiento y escalabilidad.
- CORS puede configurarse según el origen de tu frontend.
- Cumple con principios KISS, DRY, SOLID y YAGNI para un código limpio y mantenible.

---