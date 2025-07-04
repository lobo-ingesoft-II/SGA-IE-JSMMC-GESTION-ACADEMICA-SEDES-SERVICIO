from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.sedes import SedeCreate, SedeResponse, SedeUpdate
from app.services.sedes import (
    create_sede, get_sede, list_sedes,
    update_sede, delete_sede
)
from app.db import SessionLocal


router = APIRouter(tags=["Sedes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SedeResponse)
def create(sede: SedeCreate, db: Session = Depends(get_db)):
    return create_sede(db, sede)

@router.get("/", response_model=list[SedeResponse])
def list_all_sedes(db: Session = Depends(get_db)):
    return list_sedes(db)

@router.get("/{id_sede}", response_model=SedeResponse)
def get(id_sede: int, db: Session = Depends(get_db)):
    db_sede = get_sede(db, id_sede)
    if not db_sede:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    return db_sede

@router.put("/{id_sede}", response_model=SedeResponse)
def update_sede_endpoint(
    id_sede: int,
    sede_data: SedeUpdate,
    db: Session = Depends(get_db)
):
    updated = update_sede(db, id_sede, sede_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    return updated

@router.delete("/{id_sede}", status_code=204)
def delete_sede_endpoint(id_sede: int, db: Session = Depends(get_db)):
    success = delete_sede(db, id_sede)
    if not success:
        raise HTTPException(status_code=404, detail="Sede no encontrada")
    return



