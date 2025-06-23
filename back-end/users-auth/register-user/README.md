# Register User Microservice (users-auth)

Este microservicio permite registrar nuevos usuarios en el sistema de **My Pet Host**. Es responsable de validar, encriptar y almacenar usuarios en la base de datos.

---

## Tecnologías

- **FastAPI** (Python)
- **PostgreSQL**
- **bcrypt** para hashing de contraseñas
- **Docker**

---

## Estructura del proyecto

register-user/
│
├── src/
│ ├── main.py # Punto de entrada
│ ├── routes/ # users_routes.py con endpoint /register
│ ├── controllers/ # Lógica de registro y validaciones
│ ├── schemas/ # UserCreate con validaciones Pydantic
│ └── database/ # get_connection para PostgreSQL
│
├── requirements.txt
├── Dockerfile
├── .env
└── README.md


---

## Configuración del entorno

Crea un archivo `.env` con tus variables de entorno:

```env
PORT=3006
DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_pet_host
DB_USER=postgres
DB_PASSWORD=your_password

## Modo local (desarrollo)

python -m venv venv
source venv/bin/activate   # o .\venv\Scripts\activate en Windows
pip install -r requirements.txt
uvicorn src.main:app --reload --port 3006


Modo Docker (local)

docker build -t register-user .
docker run -p 3006:3006 --env-file .env register-user

## Imagen desde DockerHub (QA/Prod)

docker pull alexmpz/register-user-service:qa
docker run -d -p 3006:3006 --env-file .env alexmpz/register-user-service:qa



Endpoint: Registrar usuario

POST /api/users/register

Request body
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "MiContrasena123!",
  "role": "usuario"  // opcional (por defecto: "usuario")
}

Validaciones realizadas:
Mínimo 8 caracteres.

Al menos una mayúscula.

Al menos una minúscula.

Al menos un número.

Al menos un carácter especial (!@#$...).

Respuesta Exitosa (201):

{
  "message": "✅ User registered successfully",
  "user": {
    "id": 7,
    "username": "johndoe",
    "email": "john@example.com",
    "role": "usuario"
  }
}

| Código | Motivo                                     |
| ------ | ------------------------------------------ |
| 400    | Contraseña débil                           |
| 409    | Usuario con ese email o username ya existe |
| 422    | Formato inválido en los datos              |
| 500    | Error interno del servidor                 |

Swagger

http://localhost:3006/docs
