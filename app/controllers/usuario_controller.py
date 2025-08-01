# app/controllers/usuario_controller.py

from typing import List
from sqlmodel import Session, select
from app.models.usuario_model import Usuario

def get_all_users(session: Session) -> List[Usuario]:
    """Obtiene todos los usuarios de la base de datos."""
    usuarios = session.exec(select(Usuario)).all()
    return usuarios