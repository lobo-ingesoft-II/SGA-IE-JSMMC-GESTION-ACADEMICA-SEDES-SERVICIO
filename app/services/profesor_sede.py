import requests
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.config import settings
from app.models.profesor_sedes import ProfesorSede
from app.models.sedes import Sede
from app.services.sedes import get_sede

# Usamos la URL desde la configuración
AUTH_API_URL = settings.AUTH_API_URL

def assign_profesor_sede(db: Session, id_profesor: int, id_sede: int) -> ProfesorSede:
    # 1) Validar existencia del profesor en tu auth_api
    resp = requests.get(f"{AUTH_API_URL}/profesor/{id_profesor}")
    if resp.status_code != 200:
        raise HTTPException(status_code=404, detail="Profesor no encontrado en auth_api")

    # 2) Validar existencia de la sede local
    if not get_sede(db, id_sede):
        raise HTTPException(status_code=404, detail="Sede no encontrada")

    # 3) Crear la asignación
    asignacion = ProfesorSede(id_profesor=id_profesor, id_sede=id_sede)
    db.add(asignacion)
    db.commit()
    db.refresh(asignacion)
    return asignacion

def get_sedes_by_profesor(db: Session, id_profesor: int) -> list[Sede]:
    # 1) Validar existencia del profesor
    resp = requests.get(f"{AUTH_API_URL}/profesor/{id_profesor}")
    if resp.status_code != 200:
        raise HTTPException(status_code=404, detail="Profesor no encontrado en auth_api")

    # 2) Obtener asignaciones desde la tabla intermedia
    asignaciones = (
        db.query(ProfesorSede)
          .filter(ProfesorSede.id_profesor == id_profesor)
          .all()
    )

    # 3) Recuperar todas las sedes relacionadas
    sede_ids = [a.id_sede for a in asignaciones]
    if not sede_ids:
        return []

    sedes = db.query(Sede).filter(Sede.id_sede.in_(sede_ids)).all()
    return sedes