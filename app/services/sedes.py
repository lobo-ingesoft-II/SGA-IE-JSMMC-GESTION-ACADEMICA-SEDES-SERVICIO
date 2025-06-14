from sqlalchemy.orm import Session
from app.models.sedes import Sede
from app.schemas.sedes import SedeCreate

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