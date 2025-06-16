# models/profesor.py
from sqlalchemy import Column, Integer, ForeignKey
from app.db import Base

class Profesor(Base):
    __tablename__ = "profesores"

    id_profesor = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
