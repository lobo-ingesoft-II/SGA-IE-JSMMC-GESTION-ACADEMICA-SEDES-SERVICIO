from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db import Base

# Tabla intermedia para la relación muchos a muchos entre profesores y sedes
profesor_sedes = Table(
    "profesor_sedes",
    Base.metadata,
    Column("id_profesor", Integer, ForeignKey("usuarios.id_usuario"), primary_key=True),
    Column("id_sede", Integer, ForeignKey("sedes.id_sede"), primary_key=True),
)
