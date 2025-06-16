from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from .profesor_sede import profesor_sedes
from app.db import Base

class Sede(Base):
    __tablename__ = "sedes"

    id_sede = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)


def get_sedes_del_profesor(db: Session, profesor_id: int):
    # Buscar las sedes asociadas al profesor logueado
    return (
        db.query(Sede)
        .join(profesor_sedes, Sede.id_sede == profesor_sedes.id_sede)
        .filter(profesor_sedes.id_profesor == profesor_id)
        .all()
    )