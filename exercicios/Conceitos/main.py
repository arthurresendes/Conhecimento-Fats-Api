from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK,tags=['Padrão'],summary="Rota padrão")
async def menu():
    return {"mensagem": "Bem vindo"}

@app.get("/item/{item_id}", status_code=status.HTTP_200_OK)
async def ver_item_especifico(item_id: int):
    return {"ID item": item_id}

@app.get("/item", status_code=status.HTTP_200_OK)
async def query_parameters(pages: int = 2, size: int = 10):
    return {"Pages": pages , "Tamanho": size}

class User(BaseModel):
    name: str
    age: int
    email: str

lista_user = []

@app.post("/usuario", status_code=status.HTTP_201_CREATED)
async def inserir_user(user: User):
    if user.age > 0:
        lista_user.append(user)
        return {"Usuario": user}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Idade tem que ser maior que 0")

@app.get("/users", status_code=status.HTTP_200_OK)
async def ver_users():
    return {"Usuarios": lista_user}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1", port=8000, log_level='info', reload=True)