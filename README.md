proyecto:
  nombre: "API de Gestión de Empleados y Animales"
  descripcion: >
    Este proyecto implementa una API RESTful usando FastAPI y SQLModel
    que cumple con los requisitos académicos establecidos.
  requisitos:
    cumplidos:
      - "2 recursos: /empleados (con CRUD completo) y /animales"
      - "Filtros por path parameter y query parameter"
      - "Persistencia con base de datos relacional (SQLite)"
    opcional:
      - "Autenticación y autorización con JWT (no incluido por defecto)"
  tecnologias:
    - FastAPI
    - SQLModel
    - SQLite
    - Uvicorn

estructura:
  - .venv/: "Entorno virtual local para dependencias (no subir al repositorio)"
  - app/:
      - controllers/: "Lógica de negocio (opcional)"
      - models/: "Modelos SQLModel (Empleado, Animal)"
      - database/: "Conexión y configuración de la base de datos"
      - routes/:
          - empleados.py: "CRUD completo para empleados"
          - animales.py: "CRUD parcial para animales"
      - main.py: "Punto de entrada de la aplicación FastAPI"
  - tests/: "Tests unitarios (opcional)"
  - .env: "Archivo de entorno (vacío, para configuración local)"
  - .env.example: "Archivo de ejemplo de configuración"
  - .gitignore: "Archivos y carpetas a ignorar por Git"
  - requirements.txt: "Dependencias principales del proyecto"
  - dev-requirements.txt: "Herramientas de desarrollo (Black, Pytest, Faker)"
  - create.py: "Script de instalación y generación de estructura"
  - README.md: "Documentación general del proyecto"

instalacion:
  paso_1:
    titulo: "Crear entorno virtual"
    comandos:
      windows: "python -m venv .venv"
      linux_mac: "python3 -m venv .venv"
  paso_2:
    titulo: "Activar entorno virtual"
    comandos:
      windows_powershell: ".\\.venv\\Scripts\\Activate.ps1"
      windows_cmd: ".\\.venv\\Scripts\\activate.bat"
      linux_mac: "source .venv/bin/activate"
  paso_3:
    titulo: "Ejecutar script de configuración"
    comando: "python create.py"
  paso_4:
    titulo: "Ejecutar servidor"
    comando: "uvicorn app.main:app --reload"

documentacion:
  urls:
    swagger_ui: "http://127.0.0.1:8000/docs"
    redoc_ui: "http://127.0.0.1:8000/redoc"

endpoints:
  empleados:
    descripcion: "CRUD completo para la entidad empleados"
    rutas:
      - metodo: POST
        path: "/empleados/"
        descripcion: "Crear un nuevo empleado"
      - metodo: GET
        path: "/empleados/"
        descripcion: "Listar todos los empleados"
      - metodo: GET
        path: "/empleados/{id}"
        descripcion: "Obtener empleado por ID (path parameter)"
      - metodo: GET
        path: "/empleados?departamento=IT"
        descripcion: "Filtrar empleados por departamento (query parameter)"
      - metodo: PUT
        path: "/empleados/{id}"
        descripcion: "Actualizar un empleado existente"
      - metodo: DELETE
        path: "/empleados/{id}"
        descripcion: "Eliminar un empleado"
  animales:
    descripcion: "CRUD parcial para la entidad animales"
    rutas:
      - metodo: GET
        path: "/animales/"
        descripcion: "Listar todos los animales"

autenticacion:
  opcional: true
  tecnologias:
    - fastapi.security
    - python-jose
  descripcion: >
    Se puede añadir autenticación con JWT para proteger rutas.
    No está implementada por defecto pero puede agregarse fácilmente.

testing:
  herramientas:
    - pytest
    - faker
  descripcion: >
    Se pueden crear pruebas unitarias en la carpeta 'tests' y utilizar Faker
    para generar datos simulados durante los tests o desarrollo.

autor:
  nombre: "[Tu Nombre o Usuario]"
  año: 2025
  licencia: "Uso académico libre y personal"
