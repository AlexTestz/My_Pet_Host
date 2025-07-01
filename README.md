# 👤 Users-Auth Domain – My Pet Host

El dominio **users-auth** gestiona la autenticación, autorización y administración de usuarios en el ecosistema de **My Pet Host**. Está compuesto por microservicios independientes, cada uno con una responsabilidad clara y bien definida.

---

## 🧩 Microservicios incluidos

- **register-user:** Registro y validación de nuevos usuarios.
- **login-user:** Autenticación y generación de tokens JWT.
- **change-password:** Cambio seguro de contraseña para usuarios autenticados.
- **validate-token:** Validación y decodificación de tokens JWT.

---

## 🚀 Tecnologías principales

- **Lenguaje:** Python 3.10
- **Framework:** FastAPI
- **Base de datos:** PostgreSQL
- **Autenticación:** JWT (JSON Web Token) usando PyJWT
- **Hashing:** bcrypt para contraseñas
- **Validación:** Pydantic
- **HTTP Client:** httpx (para comunicación interna)
- **Docker:** Para despliegue y portabilidad
- **CORS:** Configurable con FastAPI Middleware

---

## 📡 Estilo de arquitectura

- **Tipo de API:** RESTful
- **Estilo arquitectónico:** Microservicios
- **Comunicación:** HTTP 
- **Separación de responsabilidades:** Cada microservicio es autónomo y desacoplado.

---

## 🏗️ Arquitectura interna

- **Patrón de arquitectura:** Separación por capas (n-capas)
  - **Rutas (API Router):** Define los endpoints HTTP
  - **Controladores:** Lógica de negocio y validaciones
  - **Esquemas:** Validación de datos con Pydantic
  - **Base de datos:** Acceso y conexión a PostgreSQL
  - **Utilidades:** Manejo de JWT, hashing, dependencias
  - **Configuración:** Variables de entorno

---

## 🧩 Patrones de diseño aplicados

- **KISS:** Código simple y directo, fácil de mantener.
- **DRY:** Reutilización de lógica y utilidades comunes.
- **SOLID:** Separación de responsabilidades en rutas, controladores y utilidades.
- **YAGNI:** Solo se implementa lo necesario para cada funcionalidad.

---

## 🔐 Seguridad

- **JWT:** Autenticación y autorización basada en tokens.
- **Hashing:** Contraseñas almacenadas y comparadas usando bcrypt.
- **Validaciones:** Contraseñas fuertes y datos de entrada validados.
- **CORS:** Configurable según el origen del frontend.

---

## 📦 Estructura general del dominio

```
users-auth/
├── register-user/
├── login-user/
├── change-password/
├── validate-token/
└── README.md
```

Cada microservicio contiene su propio código fuente, dependencias, configuración y documentación.

---

## ⚙️ Ejecución y despliegue

Cada microservicio puede ejecutarse y desplegarse de forma independiente, ya sea localmente o en contenedores Docker. Consulta el README de cada microservicio para instrucciones detalladas.

---

## 📚 Notas

- La arquitectura de microservicios permite escalar, mantener y desplegar cada componente de forma independiente.
- El dominio users-auth es fundamental para la seguridad y gestión de usuarios en **My Pet Host**.
- Cumple con principios de buenas prácticas de ingeniería de software para garantizar un código limpio, seguro y mantenible.

---