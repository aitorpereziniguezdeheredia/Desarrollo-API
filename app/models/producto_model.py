# app/models/producto_model.py

from typing import Optional
from sqlmodel import Field, SQLModel

# Modelo para la tabla de la base de datos y para las respuestas de la API (lectura)
class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    descripcion: Optional[str] = None
    precio: float
    stock: int

# Modelo para la entrada de datos al CREAR un producto (no se incluye el id)
class ProductoCreate(SQLModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int

# Modelo para la entrada de datos al ACTUALIZAR un producto (todos los campos son opcionales)
class ProductoUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None