# ✅ Validate Token Microservice – Domain: users-auth

Este microservicio verifica la validez de un token JWT y retorna información del usuario si es válido.

---

## ⚙️ Tecnologías

- FastAPI
- JWT
- Docker

---

## 📁 Estructura del proyecto

validate-token/
├── src/
│ ├── main.py
│ ├── routes/
│ ├── utils/
│ └── config/
├── requirements.txt
├── Dockerfile
├── .env
└── README.md


---

## 🔐 Variables de entorno (`.env`)

```env
PORT=3008
JWT_SECRET=myjwtsecret

 Modo local

 uvicorn src.main:app --reload --port 3008

Docker local

docker build -t validate-token .
docker run -p 3008:3008 --env-file .env validate-token

DockerHub

docker pull alexmpz/validate-token-service:qa
docker run -d -p 3008:3008 --env-file .env alexmpz/validate-token-service:qa

Endpoint
GET /api/users/validate-token
Necesita un header: Authorization: Bearer <token>

 Swagger
http://localhost:3008/docs

---

### 📦 Subir a DockerHub

```bash
docker build -t alexmpz/validate-token-service:qa .
docker push alexmpz/validate-token-service:qa
