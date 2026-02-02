from fastapi import FastAPI
from core.database import engine
from models.models import Base
from api.endpoints.routes import router

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(router)

@app.get("/")
async def menu():
    return {"Mensagem": "Bem-Vindos ao controle de estoque"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1", port=8000, log_level='info', reload=True)