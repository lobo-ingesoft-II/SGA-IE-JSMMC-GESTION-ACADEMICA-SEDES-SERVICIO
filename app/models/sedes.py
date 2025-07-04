from sqlalchemy import Column, Integer, String
from app.db import Base

class Sede(Base):
    __tablename__ = "sedes"
    id_sede = Column(Integer, primary_key=True, index=True)
    nombre  = Column(String(100), unique=True, nullable=False)



