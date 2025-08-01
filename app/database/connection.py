# app/database/connection.py

from typing import Generator
from sqlmodel import create_engine, SQLModel, Session

# Define la URL de la base de datos. Para SQLite, es un archivo en el disco.
DATABASE_URL = "sqlite:///database.db"

# Crea el motor de la base de datos.
# connect_args se necesita solo para SQLite para permitir que múltiples hilos interactúen con la misma conexión.
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

def create_db_and_tables():
    """
    Inicializa la base de datos y crea todas las tablas definidas por los modelos de SQLModel.
    Esta función se llamará al iniciar la aplicación.
    """
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """
    Generador de sesión de base de datos.
    Esta es una dependencia de FastAPI que abre una sesión por cada petición
    y la cierra al finalizar.
    """
    with Session(engine) as session:
        yield session