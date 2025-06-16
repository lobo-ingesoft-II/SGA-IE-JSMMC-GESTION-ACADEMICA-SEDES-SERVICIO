from sqlalchemy.orm import Session
from app.models.sedes import Sede
from app.schemas.sedes import SedeCreate
from app.models.profesor_sede import profesor_sedes
from app.models.profesor import Profesor


def get_profesor_id_by_usuario(db: Session, id_usuario: int) -> int | None:
    profesor = db.query(Profesor).filter(Profesor.id_usuario == id_usuario).first()
    return profesor.id_profesor if profesor else None

def create_sede(db: Session, sede: SedeCreate):
    db_sede = Sede(**sede.dict())
    db.add(db_sede)
    db.commit()
    db.refresh(db_sede)
    return db_sede

def get_sede(db: Session, id_sede: int):
    return db.query(Sede).filter(Sede.id_sede == id_sede).first()

def list_sedes(db: Session):
    return db.query(Sede).all()

def list_sedes_by_profesor(db: Session, profesor_id: int):
    resultado = (
        db.query(Sede)
        .join(profesor_sedes, Sede.id_sede == profesor_sedes.c.id_sede)
        .filter(profesor_sedes.c.id_profesor == profesor_id)
        .all()
    )
    return resultado