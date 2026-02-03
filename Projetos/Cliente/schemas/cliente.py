from pydantic import BaseModel

class CreateClie(BaseModel):
    nome: str
    idade: int
    salario: float


class CreateOut(BaseModel):
    id: int
    nome: str
    idade: int
    
    class Config:
        from_attributes = True