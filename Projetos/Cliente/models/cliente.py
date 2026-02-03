from sqlalchemy import Column, Integer, String,Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    salario = Column(Float)