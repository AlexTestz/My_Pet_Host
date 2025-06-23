# 🔐 Users Auth Domain – Microservices Architecture

Este dominio forma parte del sistema de autenticación basado en microservicios. Agrupa y coordina los siguientes servicios:

- **Register User**
- **Login User**
- **Validate Token**
- **Change Password**

Cada microservicio se implementa por separado y se comunica de forma desacoplada.

---

##  Estructura del dominio

users-auth/
├── register-user/
├── login-user/
├── validate-token/
├── change-password/
└── docker-compose.yml


---

##  Docker Compose

Este dominio utiliza Docker Compose para levantar todos los microservicios de forma unificada.

###  Levantar todos los servicios

```bash
docker-compose up --build

    Detener y eliminar contenedores
    
    docker-compose down

Endpoints de Swagger UI

Microservicio	    Puerto	    URL

Register User	    3006	    http://localhost:3006/docs
Login    User	    3007	    http://localhost:3007/docs
Validate Token	    3008	    http://localhost:3008/docs
Change   Password	3009	    http://localhost:3009/docs


Requisitos
    Docker

    Docker Compose

    Python 3.10+ (solo si deseas ejecutar manualmente sin Docker)

Notas
    Cada microservicio expone su documentación Swagger.

    El archivo docker-compose.yml orquesta los puertos y builds.

    Todos los puertos internos y externos coinciden (3006 a 3009).



