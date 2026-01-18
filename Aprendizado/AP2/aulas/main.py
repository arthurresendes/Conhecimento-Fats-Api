'''

uvicorn main:app --reload

RestAPIs: 

endpoint: link direcionando , dominio/link
Get -> Ler/pegar dados
Post -> Enviar/criar
Put/Patch -> edição
Delete -> Deletar

http://127.0.0.1:8000/docs - Para ver as documentações
'''
from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)