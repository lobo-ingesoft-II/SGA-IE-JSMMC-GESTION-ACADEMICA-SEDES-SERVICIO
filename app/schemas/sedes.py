from pydantic import BaseModel, ConfigDict

class SedeBase(BaseModel):
    nombre: str

class SedeCreate(SedeBase):
    pass

class SedeUpdate(SedeBase):
    pass

class SedeResponse(SedeBase):
    id_sede: int

    # Pydantic V2: usar ConfigDict en lugar de class Config
    model_config = ConfigDict(from_attributes=True)
