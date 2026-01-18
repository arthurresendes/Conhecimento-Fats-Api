# & "C:\Users\arregomes\Envs\famp-secao02\Scripts\Activate.ps1"
# uvicorn main:app --reload ou http://http://127.0.0.1:8000
'''
/docs -> Ver endpoints
/redoc -> Ver requisição dos endpoints
'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def raiz():
    return {"mensagem": "Você esta na raiz da secao02"}
    

@app.get("/msg")
async def mensagem():
    return {"mensagem": "Você esta na msg da secao02"}

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000,log_level="info", reload=True)