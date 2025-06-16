from pydantic import BaseModel

class SedeBase(BaseModel):
    nombre: str

class SedeCreate(SedeBase):
    pass

class SedeResponse(SedeBase):
    id_sede: int

    class Config:
        orm_mode = True