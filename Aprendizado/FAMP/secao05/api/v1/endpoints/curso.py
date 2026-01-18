from typing import List
from fastapi import APIRouter,status,HTTPException,Depends,Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from models.curso_model import CursoModel
from core.deps import get_session
from sqlmodel.sql.expression import Select,SelectOfScalar

SelectOfScalar.inherit_cache = True # Type ignore
Select.inherit_cache = True # Type ignore


router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CursoModel)
async def facul_post(curso: CursoModel,db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(nome=curso.nome, ano_entrada = curso.ano_entrada, ano_saida=curso.ano_saida, nome_faculdade=curso.nome_faculdade)
    db.add(novo_curso)
    await db.commit()
    
    return novo_curso

@router.get("/", response_model=List[CursoModel])
async def facul_get(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()
        
        return cursos

@router.get("/{curso_id}", response_model=CursoModel)
async def facul_get(curso_id: int,db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso: CursoModel = result.scalar_one_or_none()
        
        if curso:
            return curso
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado!!")

@router.put("/{curso_id}", response_model=CursoModel)
async def facul_get(curso_id: int,curso:CursoModel,db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_up: CursoModel = result.scalar_one_or_none()
        
        if curso_up:
            curso_up.nome = curso.nome
            curso_up.ano_entrada = curso.ano_entrada
            curso_up.ano_saida = curso.ano_saida
            curso_up.nome_faculdade  = curso.nome_faculdade
            
            await session.commit() 
            return curso_up
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado!!")
        
@router.delete("/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
async def facul_get(curso_id: int,db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_del: CursoModel = result.scalar_one_or_none()
        
        if curso_del:
            await session.delete(curso_del)
            await session.commit() 
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado!!")


