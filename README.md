# API de Productos con FastAPI y SQLModel
Este proyecto es una API RESTful construida con Python utilizando el framework FastAPI y el ORM SQLModel. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar) sobre un recurso de productos y listar usuarios. Utiliza una base de datos SQLite para simplificar la configuración y el despliegue.

---

## ✨ Características
Framework Moderno: Construido sobre FastAPI, que ofrece un alto rendimiento y generación automática de documentación.

ORM Intuitivo: Uso de SQLModel para una interacción sencilla y robusta con la base de datos, combinando Pydantic y SQLAlchemy.

Operaciones CRUD completas para el recurso de productos.

Filtrado de datos: El endpoint de listar productos permite filtrar por stock mínimo.

Estructura de Proyecto Organizada: El código está modularizado en controladores, modelos, rutas y configuración de base de datos para facilitar el mantenimiento.

Documentación Automática: Documentación interactiva de la API disponible en /docs (Swagger UI) y /redoc.

---

## 📂 Estructura del Proyecto
El proyecto sigue una estructura modular para separar las responsabilidades y mantener el código limpio y escalable.
```
.
├── app/
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada de la aplicación FastAPI
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── producto_controller.py  # Lógica de negocio para productos
│   │   └── usuario_controller.py   # Lógica de negocio para usuarios
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py         # Configuración y sesión de la base de datos
│   ├── models/
│   │   ├── __init__.py
│   │   ├── producto_model.py     # Modelo de datos para Producto
│   │   └── usuario_model.py      # Modelo de datos para Usuario
│   └── routes/
│       ├── __init__.py
│       ├── producto_routes.py    # Endpoints para /productos
│       └── usuario_routes.py     # Endpoints para /usuarios
└── README.md                   # Este archivo
```

---

## 🛠️ Tecnologías Utilizadas
Python 3.10+

FastAPI: Framework web para construir APIs.

SQLModel: ORM para interactuar con la base de datos.

Uvicorn: Servidor ASGI para ejecutar la aplicación.

SQLite: Motor de base de datos basado en ficheros.

---

## 🚀 Instalación y Ejecución
Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

1. Prerrequisitos
Asegúrate de tener instalado Python 3.10 o una versión superior.

2. Clonar el Repositorio
Si tienes el proyecto en un repositorio Git, clónalo. Si no, simplemente crea los archivos y directorios como se describió anteriormente.

Bash

git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_DIRECTORIO>
3. Crear un Entorno Virtual
Es una buena práctica trabajar dentro de un entorno virtual para aislar las dependencias del proyecto.

Bash

### Crear el entorno virtual
python -m venv venv

### Activarlo (en Windows)
.\venv\Scripts\activate

### Activarlo (en macOS/Linux)
source venv/bin/activate
4. Instalar Dependencias
Crea un archivo requirements.txt en la raíz del proyecto con el siguiente contenido:

requirements.txt

Plaintext

fastapi
uvicorn[standard]
sqlmodel
Luego, instala las dependencias usando pip:

Bash

pip install -r requirements.txt
5. Ejecutar la Aplicación
Una vez instaladas las dependencias, puedes iniciar el servidor de desarrollo desde el directorio raíz del proyecto.

Bash

fastapi dev app/main.py
app.main: se refiere al archivo main.py dentro del directorio app.

app: es la instancia de FastAPI creada dentro de main.py.

--reload: reinicia el servidor automáticamente cada vez que detecta un cambio en el código.

La API estará disponible en http://127.0.0.1:8000 y en http://127.0.0.1:8000/docs.

---

## 📖 Documentación de la API
FastAPI genera automáticamente la documentación interactiva de la API. Una vez que el servidor esté en ejecución, puedes acceder a ella en las siguientes URLs:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Desde Swagger UI, puedes ver todos los endpoints, sus parámetros, y probarlos directamente desde el navegador.

---

## 🔀 Endpoints de la API
Aquí se detallan todos los endpoints disponibles.

Productos (/productos)
Método	Ruta	Descripción	Body (Ejemplo)	Respuesta Exitosa (Ejemplo)
POST	/	Crea un nuevo producto.	{"nombre": "Laptop Pro", "precio": 1200.50, "stock": 50}	201 Created con el objeto del producto creado.
GET	/	Obtiene una lista de todos los productos.	-	200 OK con un array de productos.
GET	/?stock_minimo=10	Obtiene productos con stock mayor o igual al valor.	-	200 OK con un array de productos filtrados.
GET	/{producto_id}	Obtiene un producto por su ID.	-	200 OK con el objeto del producto.
PUT	/{producto_id}	Actualiza un producto existente por su ID.	{"precio": 1150.00, "stock": 45}	200 OK con el objeto del producto actualizado.
DELETE	/{producto_id}	Elimina un producto por su ID.	-	200 OK con el objeto del producto eliminado.

Exportar a Hojas de cálculo
Nota: Para los endpoints que reciben un producto_id, se devolverá un 404 Not Found si el producto no existe.

Usuarios (/usuarios)
Método	Ruta	Descripción	Respuesta Exitosa (Ejemplo)
GET	/	Obtiene una lista de todos los usuarios.	200 OK con un array de usuarios.
