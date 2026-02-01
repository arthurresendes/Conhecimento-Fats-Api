from fastapi import FastAPI, status

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1", port=8000, log_level='info', reload=True)