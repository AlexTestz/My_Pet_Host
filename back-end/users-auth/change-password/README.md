# Change Password Microservice – Domain: users-auth

Permite a los usuarios autenticados cambiar su contraseña validando el token y actualizando la base de datos.

---

## Tecnologías

- FastAPI
- PostgreSQL
- bcrypt
- JWT
- Docker

---

##  Estructura del proyecto

change-password/
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
PORT=3009
DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_pet_host
DB_USER=postgres
DB_PASSWORD=your_password
JWT_SECRET=myjwtsecret


 Modo local

uvicorn src.main:app --reload --port 3009

Dockerlocal

docker build -t change-password .
docker run -p 3009:3009 --env-file .env change-password

Dockerhub

docker pull alexmpz/change-password-service:qa
docker run -d -p 3009:3009 --env-file .env alexmpz/change-password-service:qa

Endpoint
PUT /api/users/change-password

{
  "old_password": "MiContrasena123!",
  "new_password": "NuevaContrasena456!"
}

 Swagger
http://localhost:3009/docs


---

### Subir a DockerHub

```bash
docker build -t alexmpz/change-password-service:qa .
docker push alexmpz/change-password-service:qa
