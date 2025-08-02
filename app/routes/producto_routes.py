# app/routes/producto_routes.py

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.database.connection import get_session
# Importamos los modelos necesarios
from app.models.producto_model import Producto, ProductoCreate, ProductoUpdate
from app.controllers import producto_controller

router = APIRouter(
    prefix="/productos",
    tags=["Productos"],
    responses={404: {"description": "No encontrado"}},
)

# 👇 CAMBIO AQUÍ: Usamos ProductoCreate para el body de la petición
@router.post("/", response_model=Producto, status_code=status.HTTP_201_CREATED)
def create_new_product(producto: ProductoCreate, session: Session = Depends(get_session)):
    """Crea un nuevo producto. El ID es autogenerado."""
    return producto_controller.create_product(producto_create=producto, session=session)


@router.get("/", response_model=List[Producto])
def read_all_products(stock_minimo: Optional[int] = None, session: Session = Depends(get_session)):
    """Lee todos los productos, con opción de filtrar por stock mínimo."""
    return producto_controller.get_all_products(stock_minimo=stock_minimo, session=session)


@router.get("/{producto_id}", response_model=Producto)
def read_product_by_id(producto_id: int, session: Session = Depends(get_session)):
    """Lee un producto específico por su ID."""
    producto = producto_controller.get_product_by_id(producto_id=producto_id, session=session)
    if not producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return producto


# 👇 CAMBIO AQUÍ: Usamos ProductoUpdate para el body de la petición
@router.put("/{producto_id}", response_model=Producto)
def update_existing_product(producto_id: int, producto: ProductoUpdate, session: Session = Depends(get_session)):
    """Actualiza un producto existente."""
    updated_producto = producto_controller.update_product(producto_id=producto_id, producto_update=producto, session=session)
    if not updated_producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return updated_producto


@router.delete("/{producto_id}", response_model=Producto)
def delete_existing_product(producto_id: int, session: Session = Depends(get_session)):
    """Elimina un producto existente."""
    deleted_producto = producto_controller.delete_product(producto_id=producto_id, session=session)
    if not deleted_producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return deleted_producto