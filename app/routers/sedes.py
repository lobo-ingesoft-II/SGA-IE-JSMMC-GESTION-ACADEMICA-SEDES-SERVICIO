from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.sedes import SedeCreate, SedeResponse
from app.services.sedes import create_sede, get_sede, list_sedes
from app.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SedeResponse)
def create(sede: SedeCreate, db: Session = Depends(get_db)):
    return create_sede(db, sede)

@router.get("/{id_sede}", response_model=SedeResponse)
def get(id_sede: int, db: Session = Depends(get_db)):
    db_sede = get_sede(db, id_sede)
    if not db_sede:
        raise HTTPException(status_code=404, detail="Sede not found")
    return db_sede

@router.get("/", response_model=list[SedeResponse])
def list_all(db: Session = Depends(get_db)):
    return list_sedes(db)