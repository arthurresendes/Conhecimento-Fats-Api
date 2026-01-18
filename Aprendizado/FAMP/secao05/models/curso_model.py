from typing import Optional
from sqlmodel import Field,SQLModel

class CursoModel(SQLModel, table=True):
    __tablename__: str = "faculdades"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    ano_entrada: int
    ano_saida: int
    nome_faculdade: str