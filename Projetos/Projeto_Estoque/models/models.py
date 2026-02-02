from core import database
from sqlalchemy import Column, Integer, String,Float, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    
    id = Column(Integer,primary_key=True, autoincrement=True)
    nome  = Column(String)
    preco = Column(Float)
    quantidade = Column(Integer)
    promocao = Column(Boolean)