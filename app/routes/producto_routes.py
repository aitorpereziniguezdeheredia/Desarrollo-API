# app/routes/producto_routes.py

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.database.connection import get_session
from app.models.producto_model import Producto
from app.controllers import producto_controller

router = APIRouter(
    prefix="/productos",
    tags=["Productos"],
    responses={404: {"description": "No encontrado"}},
)

@router.post("/", response_model=Producto, status_code=status.HTTP_201_CREATED)
def create_new_product(producto: Producto, session: Session = Depends(get_session)):
    """Crea un nuevo producto."""
    return producto_controller.create_product(producto=producto, session=session)


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


@router.put("/{producto_id}", response_model=Producto)
def update_existing_product(producto_id: int, producto: Producto, session: Session = Depends(get_session)):
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