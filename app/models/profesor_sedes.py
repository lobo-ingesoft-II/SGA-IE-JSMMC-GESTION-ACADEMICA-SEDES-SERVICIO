from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class ProfesorSede(Base):
    __tablename__ = "profesor_sede"

    id_profesor_sede = Column(Integer, primary_key=True, index=True)
    id_profesor       = Column(Integer, nullable=False)
    id_sede           = Column(Integer, ForeignKey("sedes.id_sede"), nullable=False)

    sede = relationship("Sede", backref="profesores_asignados")