#  Login User Microservice – Domain: users-auth.

Este microservicio se encarga de la autenticación de usuarios, validando credenciales y generando tokens JWT para sesiones seguras.

---

## Tecnologías

- FastAPI
- PostgreSQL
- JWT
- Docker

---

##  Estructura del proyecto

login-user/
├── src/
│ ├── main.py
│ ├── routes/
│ ├── controllers/
│ ├── schemas/
│ └── database/
├── requirements.txt
├── Dockerfile
├── .env
└── README.md


---

##  Variables de entorno (`.env`)

```env
PORT=3007
DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_pet_host
DB_USER=postgres
DB_PASSWORD=your_password
JWT_SECRET=myjwtsecret

Modo local (desarrollo)

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload --port 3007

Docker (local)

docker build -t login-user .
docker run -p 3007:3007 --env-file .env login-user

DockerHub (QA/Prod)

docker pull alexmpz/login-user-service:qa
docker run -d -p 3007:3007 --env-file .env alexmpz/login-user-service:qa

Endpoint
POST /api/users/login

{
  "email": "john@example.com",
  "password": "MiContrasena123!"
}

Swagger

http://localhost:3007/docs


---

###  Subir a DockerHub

```bash
docker build -t alexmpz/login-user-service:qa .
docker push alexmpz/login-user-service:qa


