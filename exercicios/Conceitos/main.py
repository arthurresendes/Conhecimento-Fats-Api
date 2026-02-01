from fastapi import FastAPI, status

app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK,tags=['Padrão'],summary="Rota padrão")
async def menu():
    return {"mensagem": "Bem vindo"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1", port=8000, log_level='info', reload=True)