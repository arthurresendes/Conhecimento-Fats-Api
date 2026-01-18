from fastapi import FastAPI
from fastapi import status, HTTPException,Response,Path,Query,Header,Depends
from models import Curso
from typing import Optional, Any,Dict,List
from time import sleep
from models import cursos
# & "C:\Users\arthu\Envs\famp-secao03\Scripts\Activate.ps1"


app = FastAPI(title="Aprendizado Fast Api",
              version="0.0.1",
              description="Uma API para estudo do FastApi"
              )


@app.get('/cursos', description="Retorna todos os cursos ou lista vazia", summary="Retorna todos os cursos", response_model=Dict[int,Curso], response_description="Cursos encontrados")
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_cursos_id(curso_id:int = Path(default=None, title="ID do curso", description="Deve ser entre 1 e 2", gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id:int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso

@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int,curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        curso.id = curso_id
        return curso
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curso com o id {curso_id}")

@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id:int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")

@app.get("/calculadora")
async def calcular(a:int = Query(default=None, gt=5) ,b:int = Query(default=None, gt=10),x_arthur: str = Header(default=None),c: Optional[int] = None):
    if c:
        soma = a+b + c
    else:
        soma = a+b
    print(f"x_arthur , {x_arthur}")
    return {"resultado": soma}
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, debug=True, reload=True)