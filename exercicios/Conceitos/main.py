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
id_users = 0

@app.post("/usuario", status_code=status.HTTP_201_CREATED)
async def inserir_user(user: User):
    global id_users
    if user.age > 0:
        id_users += 1
        lista_user.append({"Id": id_users, "Informações": user})
        return {"ID": id_users,"Usuario": user}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Idade tem que ser maior que 0")

@app.get("/usuario", status_code=status.HTTP_200_OK)
async def ver_users():
    return {"Usuarios": lista_user}

@app.get("/usuario/{user_id}", status_code=status.HTTP_200_OK)
async def ver_user_id(user_id: int):
    for i in lista_user:
        if i["Id"] == user_id:
            return {"Usuario": i}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado")

class Person(BaseModel):
    name: str
    email: str
    password: str

class PersonOut(BaseModel):
    name: str
    email: str

@app.post("/person", response_model=PersonOut, status_code=status.HTTP_201_CREATED,)
async def adicionar_person(person: Person):
    return person

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1", port=8000, log_level='info', reload=True)