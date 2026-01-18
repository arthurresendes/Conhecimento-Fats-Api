from typing import Optional
from pydantic import BaseModel,validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    
    @validator('titulo')
    def validar_titulo(cls,value):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O titulo deve ter pelo menos tres palavras')
        if value.islower():
            raise ValueError("O titulo tem que ser capitalizado , ou seja inicias maisculas")
        return value
    
    @validator('aulas')
    def validar_aulas(cls,value:int):
        if value < 12:
            raise ValueError("Deve ter no minimo 12 aulas")
        return value
    
    @validator('horas')
    def validar_horas(cls,value:int):
        if value < 10:
            raise ValueError("O curso deve ter no minimo 10 horas")
        return value


cursos = [
    Curso(id=1,titulo="Programação em Python", aulas=42,horas=56),
    Curso(id=2,titulo="Programação em C", aulas=52,horas=67)
]