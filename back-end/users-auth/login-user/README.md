# 🔐 Login User Microservice – users-auth

Permite a los usuarios autenticarse, generando y validando tokens JWT para el acceso seguro a los recursos del sistema.

---

## 🚀 Tecnologías

- **Lenguaje:** Python 3.10
- **Framework:** FastAPI
- **Base de datos:** PostgreSQL
- **Autenticación:** JWT (JSON Web Token) usando PyJWT
- **Hashing:** bcrypt para contraseñas
- **HTTP Client:** httpx (para comunicación con otros microservicios)
- **CORS:** Configurado con FastAPI Middleware

---

## 📡 Estilo de arquitectura

- **Tipo de API:** RESTful
- **Estilo arquitectónico:** Microservicios
- **Comunicación:** HTTP 
- **Endpoints expuestos:**  
  - `/api/auth/login` (POST)  
  - `/api/auth/validate-token` (GET)

  POST http://3.214.168.136:8000/api/users/login 

  BODY
{
  "username_or_email": "alexadmin@hotmail.com",
  "password": "EJEMPLO!"
}

GET http://3.214.168.136:8000/api/users/validate-token

HEADERS :  Authorization  Bearer  token

---

## 🏗️ Arquitectura interna

- **Patrón de arquitectura:** Separación por capas (n-capas)
  - **Rutas (API Router):** Define los endpoints HTTP
  - **Controladores:** Lógica de negocio
  - **Esquemas:** Validación de datos con Pydantic
  - **Base de datos:** Acceso y conexión
  - **Utilidades:** Manejo de JWT
  - **Configuración:** Variables de entorno

---

## 🧩 Patrones de diseño aplicados

- **KISS:** Código simple y directo, fácil de mantener.
- **DRY:** Reutilización de lógica y utilidades comunes.
- **SOLID:** Separación de responsabilidades en rutas, controladores y utilidades.
- **YAGNI:** Solo se implementa lo necesario para el login y validación de token.

---

## 🔐 Seguridad

- **JWT:** Se genera y valida el token en cada autenticación, extrayendo el user_id del payload.
- **CORS:** Permite solicitudes desde cualquier origen (`allow_origins=["*"]`), configurable para producción.
- **Hashing:** Contraseñas almacenadas y comparadas usando bcrypt.

---

## 📦 Estructura del proyecto

```
login-user/
├── src/
│   ├── main.py
│   ├── routes/
│   ├── controllers/
│   ├── schemas/
│   ├── database/
│   ├── utils/
│   └── config/
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

## ⚙️ Ejecución

**Modo local:**
```bash
uvicorn src.main:app --reload --port 3008
```

**Docker local:**
```bash
docker build -t login-user .
docker run -p 3008:3008 --env-file .env login-user
```

---

## 🛠️ Endpoints principales

- `POST /api/users/login`  
  Autentica al usuario y retorna un JWT.

- `GET /api/users/validate-token`  
  Valida el JWT enviado en el header Authorization.

**Swagger:**  
http://3.223.253.161:3007/docs 
http://3.223.253.161:3008/docs 
---

## 📚 Notas

- Arquitectura desacoplada, cada microservicio es independiente.
- El patrón n-capas facilita el mantenimiento y escalabilidad.
- JWT asegura que solo usuarios autenticados puedan acceder a recursos protegidos.
- CORS abierto para desarrollo, restringir en producción.
- Cumple con principios KISS, DRY, SOLID y YAGNI para un código limpio y mantenible.

---