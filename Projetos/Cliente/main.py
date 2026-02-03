from fastapi import FastAPI
from core.database import engine
from models.cliente import Base
from api.endpoint.rotas import router

app = FastAPI(title="Base Clientes", description="Projeto de controle de Clientes via FastApi", version="1.0.0", summary="API que faz um CRUD sobre os clientes diretamente de um sqlite assincrono", contact={"name": "Arthur Resende", "Linkedin": "www.linkedin.com/in/arthur-resende-gomes"})

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(router)

@app.get("/",tags=["Main"] ,summary="Menu Inicial")
async def menu():
    return {"Mensagem": "Bem-Vindos ao controle de clientes"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1", port=8000, log_level='info', reload=True)