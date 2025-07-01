# 🔑 Change Password Microservice – users-auth

Permite a los usuarios autenticados cambiar su contraseña validando el token JWT y actualizando la base de datos.

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
- **Comunicación:** HTTP (sin WebSocket, gRPC, SOAP ni GraphQL)
- **Endpoints expuestos:** `/api/users/change-password` (PUT)

PUT http://3.214.168.136:8000/api/users/change-password
HEADERS  Authorization          Bearer TOKEN
BODY
{
  "old_password": "admin123!",
  "new_password": "Admin123!"
}


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
- **YAGNI:** Solo se implementa lo necesario para el cambio de contraseña y validación.

---

## 🔐 Seguridad

- **JWT:** Se valida el token en cada petición protegida, extrayendo el user_id del payload.
- **CORS:** Permite solicitudes desde cualquier origen (`allow_origins=["*"]`), configurable para producción.
- **Hashing:** Contraseñas almacenadas y comparadas usando bcrypt.

---

## 📦 Estructura del proyecto

```
change-password/
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
uvicorn src.main:app --reload --port 3009
```

**Docker local:**
```bash
docker build -t change-password .
docker run -p 3009:3009 --env-file .env change-password
```

**DockerHub:**
```bash
docker pull alexmpz/change-password-service:qa
docker run -d -p 3009:3009 --env-file .env alexmpz/change-password-service:qa
```

---

## 🛠️ Endpoint principal

- `PUT /api/users/change-password`

**Body ejemplo:**
```json
{
  "old_password": "MiContrasena123!",
  "new_password": "NuevaContrasena456!"
}
```

**Swagger:**  
http://3.223.253.161:3009/docs 

---

## ☁️ Subir a DockerHub

```bash
docker build -t alexmpz/change-password-service:qa .
docker push alexmpz/change-password-service:qa
```

---

## 📚 Notas

- Arquitectura desacoplada, cada microservicio es independiente.
- El patrón n-capas facilita el mantenimiento y escalabilidad.
- JWT asegura que solo usuarios autenticados puedan cambiar su contraseña.
- CORS abierto para desarrollo, restringir en producción.
- Cumple con principios KISS, DRY, SOLID y YAGNI para un código limpio y