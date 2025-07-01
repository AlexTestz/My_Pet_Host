# 🛡️ Validate Token Microservice (users-auth)

Este microservicio permite validar tokens JWT para asegurar el acceso autenticado a los recursos del sistema **My Pet Host**.

---

## 🚀 Tecnologías

- **Lenguaje:** Python 3.10
- **Framework:** FastAPI
- **Base de datos:** PostgreSQL 
- **Autenticación:** JWT (JSON Web Token) usando PyJWT
- **Validación:** Pydantic
- **Docker:** Para despliegue y portabilidad

---

## 📡 Estilo de arquitectura

- **Tipo de API:** RESTful
- **Estilo arquitectónico:** Microservicios
- **Comunicación:** HTTP
- **Endpoint expuesto:** `/api/auth/validate-token` (GET)

---

## 🏗️ Arquitectura interna

- **Patrón de arquitectura:** Separación por capas (n-capas)
  - **Rutas (API Router):** Define los endpoints HTTP
  - **Controladores:** Lógica de validación de token
  - **Esquemas:** Validación de datos con Pydantic
  - **Utilidades:** Manejo y decodificación de JWT

---

## 🧩 Patrones de diseño aplicados

- **KISS:** Código simple y directo, fácil de mantener.
- **DRY:** Reutilización de lógica y utilidades comunes.
- **SOLID:** Separación de responsabilidades en rutas, controladores y utilidades.
- **YAGNI:** Solo se implementa lo necesario para la validación de token.

---

## 🔐 Seguridad

- **JWT:** Se valida el token en cada petición protegida, extrayendo el user_id y verificando su validez y expiración.
- **CORS:** Configurable con FastAPI Middleware (agregar según necesidad del frontend).

---

## 📦 Estructura del proyecto

```
validate-token/
├── src/
│   ├── main.py
│   ├── routes/
│   ├── controllers/
│   ├── schemas/
│   └── utils/
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
uvicorn src.main:app --reload --port 3010
```

**Docker local:**
```bash
docker build -t validate-token .
docker run -p 3010:3010 --env-file .env validate-token
```

---

## 🛠️ Endpoint principal

- `GET /api/auth/validate-token`

GET http://3.214.168.136:8000/api/users/validate-token

HEADERS Authorization           Bearer  TOKEN

**Headers requeridos:**
```
Authorization: Bearer <token>
```

**Respuesta Exitosa (200):**
```json
{
  "message": "✅ Token válido",
  "user_id": 7,
  "exp": 1719876543
}
```

| Código | Motivo                        |
| ------ | ----------------------------- |
| 401    | Token inválido o expirado     |
| 422    | Formato inválido en el token  |

**Swagger:**  
http://3.223.253.161:3008/docs

---

## 📚 Notas

- Arquitectura desacoplada, cada microservicio es independiente.
- El patrón n-capas facilita el mantenimiento y escalabilidad.
- CORS puede configurarse según el origen de tu frontend.
- Cumple con principios KISS, DRY, SOLID y YAGNI para un código limpio y mantenible.

---