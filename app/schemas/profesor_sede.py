from pydantic import BaseModel, ConfigDict

class ProfesorSedeBase(BaseModel):
    id_profesor: int
    id_sede: int

class ProfesorSedeCreate(ProfesorSedeBase):
    """Esquema para asignar un profesor a una sede."""
    pass

class ProfesorSedeResponse(ProfesorSedeBase):
    id_profesor_sede: int

    # Para permitir conversiones desde atributos del ORM
    model_config = ConfigDict(from_attributes=True)