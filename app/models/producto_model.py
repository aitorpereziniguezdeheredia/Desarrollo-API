# app/models/producto_model.py

from typing import Optional
from sqlmodel import Field, SQLModel

class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    descripcion: Optional[str] = None
    precio: float
    stock: int