# app/controllers/producto_controller.py

from typing import List, Optional
from sqlmodel import Session, select
# Importamos los nuevos modelos
from app.models.producto_model import Producto, ProductoCreate, ProductoUpdate 

# La función ahora espera un objeto del tipo ProductoCreate
def create_product(producto_create: ProductoCreate, session: Session) -> Producto:
    """Crea un nuevo producto en la base de datos."""
    # Convertimos el modelo de creación al modelo de tabla
    db_producto = Producto.model_validate(producto_create)
    
    session.add(db_producto)
    session.commit()
    session.refresh(db_producto)
    return db_producto

def get_all_products(stock_minimo: Optional[int], session: Session) -> List[Producto]:
    """Obtiene todos los productos, con un filtro opcional por stock mínimo."""
    query = select(Producto)
    if stock_minimo is not None:
        query = query.where(Producto.stock >= stock_minimo)
    
    productos = session.exec(query).all()
    return productos

def get_product_by_id(producto_id: int, session: Session) -> Optional[Producto]:
    """Obtiene un producto por su ID."""
    producto = session.get(Producto, producto_id)
    return producto

# La función ahora espera un objeto del tipo ProductoUpdate
def update_product(producto_id: int, producto_update: ProductoUpdate, session: Session) -> Optional[Producto]:
    """Actualiza un producto existente en la base de datos."""
    db_producto = session.get(Producto, producto_id)
    if not db_producto:
        return None
    
    # Obtenemos los datos del producto a actualizar, excluyendo los no establecidos (None)
    producto_data = producto_update.model_dump(exclude_unset=True)
    
    for key, value in producto_data.items():
        setattr(db_producto, key, value)
        
    session.add(db_producto)
    session.commit()
    session.refresh(db_producto)
    return db_producto

def delete_product(producto_id: int, session: Session) -> Optional[Producto]:
    """Elimina un producto de la base de datos."""
    producto = session.get(Producto, producto_id)
    if not producto:
        return None
        
    session.delete(producto)
    session.commit()
    return producto