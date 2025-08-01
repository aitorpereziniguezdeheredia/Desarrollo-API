# app/routes/usuario_routes.py

from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database.connection import get_session
from app.models.usuario_model import Usuario
from app.controllers import usuario_controller

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.get("/", response_model=List[Usuario])
def read_all_users(session: Session = Depends(get_session)):
    """Lee todos los usuarios."""
    return usuario_controller.get_all_users(session=session)