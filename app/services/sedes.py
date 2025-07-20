from sqlalchemy.orm import Session
from app.models.sedes import Sede
from app.schemas.sedes import SedeCreate, SedeUpdate

def create_sede(db: Session, sede: SedeCreate):
    db_sede = Sede(**sede.model_dump())
    db.add(db_sede)
    db.commit()
    db.refresh(db_sede)
    return db_sede

def get_sede(db: Session, id_sede: int):
    return db.query(Sede).filter(Sede.id_sede == id_sede).first()

def get_sede_by_name(db: Session, name: str):
    return db.query(Sede).filter(Sede.nombre == name).first()

def list_sedes(db: Session):
    return db.query(Sede).all()

def update_sede(db: Session, id_sede: int, sede_data: SedeUpdate):
    db_sede = get_sede(db, id_sede)
    if not db_sede:
        return None
    for key, value in sede_data.model_dump().items():
        setattr(db_sede, key, value)
    db.commit()
    db.refresh(db_sede)
    return db_sede

def delete_sede(db: Session, id_sede: int) -> bool:
    db_sede = get_sede(db, id_sede)
    if not db_sede:
        return False
    db.delete(db_sede)
    db.commit()
    return True
