from pydantic import BaseModel

class ProdutoCreate(BaseModel):
    nome: str
    preco: float
    quantidade: int
    promocao: bool


class ProdutoOut(BaseModel):
    id: int
    nome: str
    preco: float
    
    class Config:
        from_attributes = True

