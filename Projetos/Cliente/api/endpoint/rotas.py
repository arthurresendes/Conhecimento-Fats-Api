from fastapi import APIRouter,status,HTTPException,Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from models.cliente import Cliente
from schemas.cliente import CreateClie,CreateOut

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/",status_code=status.HTTP_200_OK,summary="Rota padrão")
async def padrao():
    return {"mensagem": "Rota padroa clientes"}

@router.get("/clie", status_code=status.HTTP_200_OK, summary="Lista de todos clientes")
async def lista_clientes(db: AsyncSession = Depends(get_db)):
    query = await db.execute(select(Cliente))
    return query.scalars().all()

@router.get("/clie/{clie_id}", status_code=status.HTTP_200_OK, summary="Um cliente especifico")
async def lista_cliente_especifico(clie_id: int,db: AsyncSession = Depends(get_db)):
    query = await db.execute(select(Cliente).filter(Cliente.id == clie_id))
    return query.scalars().first()

@router.post("/clie", status_code=status.HTTP_201_CREATED, response_model=CreateOut, summary="Criar cliente")
async def criar_cliente(modelo: CreateClie, db: AsyncSession = Depends(get_db)):
    novo_cliente = Cliente(**modelo.model_dump())
    db.add(novo_cliente)
    await db.commit()
    await db.refresh(novo_cliente)
    return novo_cliente

@router.put("/clie/{clie_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Atualizar cliente")
async def atualizar_cliente(clie_id: int,modelo: CreateClie, db: AsyncSession = Depends(get_db)):
    query  = select(Cliente).filter(Cliente.id == clie_id)
    res = await db.execute(query)
    clie_up = res.scalars().one_or_none()

    if not clie_up:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )

    if modelo.nome is not None:
        clie_up.nome = modelo.nome
    if modelo.idade is not None:
        clie_up.idade = modelo.idade
    if modelo.salario is not None:
        clie_up.salario = modelo.salario

    await db.commit()
    await db.refresh(clie_up)


@router.delete("/clie/{clie_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Deletar cliente")
async def deletar_cliente(clie_id: int, db: AsyncSession = Depends(get_db)):
    query  = select(Cliente).filter(Cliente.id == clie_id)
    res = await db.execute(query)
    clie_del = res.scalars().one_or_none()

    if not clie_del:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente não encontrado"
        )

    await db.delete(clie_del)
    await db.commit()



