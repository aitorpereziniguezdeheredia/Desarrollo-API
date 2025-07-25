# 🚀 API de Gestión de Empleados y Animales (FastAPI + SQLModel)

Este proyecto implementa una API RESTful usando **FastAPI** y **SQLModel** que cumple con los siguientes requisitos:

## ✅ Requisitos del Trabajo

- [x] 2 recursos: `/empleados` (con CRUD completo) y `/animales`
- [x] Filtros por **path parameter** y **query parameter**
- [x] Persistencia de datos con **base de datos relacional (SQLite)**
- [ ] (Opcional) Autenticación y autorización con JWT *(no incluido por defecto, pero fácil de añadir)*

---

## 🏗️ Estructura del Proyecto

app/
├── controllers/ # (Opcional: lógica de negocio separada)
├── models/ # Modelos SQLModel (Empleado, Animal)
├── database/ # Conexión y setup de la base de datos
├── routes/ # Endpoints de la API
│ ├── empleados.py # CRUD completo
│ └── animales.py # CRUD parcial
├── main.py # Punto de entrada de FastAPI
tests/ # Tests unitarios (opcional)
.env # Variables de entorno vacías
.env.example # Ejemplo de configuración
.gitignore # Archivos y carpetas ignoradas por Git
requirements.txt # Dependencias principales
dev-requirements.txt # Herramientas de desarrollo (Black, Faker, Pytest)
create.py # Script de generación de estructura y setup

yaml
Copiar
Editar

---

## ⚙️ Tecnologías Usadas

- **FastAPI** – Framework moderno y veloz para APIs
- **SQLModel** – ORM moderno que combina Pydantic + SQLAlchemy
- **SQLite** – Base de datos relacional ligera
- **Uvicorn** – Servidor ASGI para desarrollo

---

## 🚀 Instrucciones de Instalación y Ejecución

### 1. Ejecutar el script de configuración

Este script creará la estructura del proyecto, instalará las dependencias y generará archivos básicos:

```bash
python create.py
Esto hará lo siguiente:

Instalar dependencias (fastapi, sqlmodel, etc.)

Crear estructura de carpetas

Generar .env, .gitignore, requirements.txt, etc.

2. Agregar el código fuente
Luego del script, debes agregar los siguientes archivos dentro de:

app/models/ – Modelos de empleados y animales

app/routes/ – Endpoints CRUD

app/database/ – Conexión a la base de datos

app/main.py – Archivo principal de la app

📌 Todos estos archivos están listos más abajo en esta documentación si deseas copiarlos directamente.

🧪 Ejecutar la aplicación
Una vez completado el código:

bash
Copiar
Editar
uvicorn app.main:app --reload
La API estará disponible en: http://127.0.0.1:8000

Acceder a la documentación interactiva:
Swagger: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

🔍 Rutas disponibles
/empleados (CRUD completo)
Método	Ruta	Descripción
POST	/empleados/	Crear un nuevo empleado
GET	/empleados/	Listar todos los empleados
GET	/empleados/{id}	Obtener empleado por ID (path parameter)
GET	/empleados?departamento=IT	Filtrar por departamento (query param)
PUT	/empleados/{id}	Actualizar un empleado
DELETE	/empleados/{id}	Eliminar un empleado

/animales (CRUD parcial)
Método	Ruta	Descripción
GET	/animales/	Listar todos los animales

🛡️ (Opcional) Autenticación con JWT
Puedes añadir autenticación para proteger endpoints. Usa paquetes como:

python-jose – Para generar y verificar JWT

fastapi.security – Para dependencias de seguridad