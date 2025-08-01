# app/main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database.connection import create_db_and_tables
from app.routes import producto_routes, usuario_routes

# El 'lifespan' manager reemplaza los eventos 'startup' y 'shutdown'
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código a ejecutar antes de que la aplicación inicie
    print("Iniciando aplicación y creando base de datos si no existe...")
    create_db_and_tables()
    yield
    # Código a ejecutar cuando la aplicación se apaga (si es necesario)
    print("Apagando aplicación.")


app = FastAPI(
    title="API KÖRE-Streetwear",
    description="Una API para gestionar productos y usuarios.",
    version="0.0.1",
    lifespan=lifespan
)

# Incluir las rutas de los diferentes módulos
app.include_router(producto_routes.router)
app.include_router(usuario_routes.router)

@app.get("/", tags=["Root"])
def read_root():
    """Endpoint principal de bienvenida."""
    return {"mensaje": "Bienvenido a la API de Productos y Usuarios"}