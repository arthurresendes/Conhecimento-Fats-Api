from sqlalchemy import select
from fastapi import APIRouter,status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.schemas import ProdutoOut,ProdutoCreate
from models.models import Produto
from core.database import get_db

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/prod", status_code=status.HTTP_201_CREATED, response_model=ProdutoOut)
async def cadastrar(prod: ProdutoCreate, db: AsyncSession = Depends(get_db)):
    novo_produto = Produto(**prod.model_dump())
    db.add(novo_produto) # Transforma o schema Pydantic em um modelo SQLAlchemy
    await db.commit()
    await db.refresh(novo_produto) # Atualiza o objeto para carregar o ID e campos gerados pelo banco
    return novo_produto

@router.get("/prods", status_code=status.HTTP_200_OK)
async def ver_produtos(db: AsyncSession = Depends(get_db)):
    resultado = await db.execute(select(Produto))
    return resultado.scalars().all()

@router.get("/prods/{prod_id}", status_code=status.HTTP_200_OK)
async def ver_prod_especifico(prod_id: int, db: AsyncSession = Depends(get_db)):
    query  = select(Produto).filter(Produto.id == prod_id)
    resultado = await db.execute(query)
    return resultado.scalars().first()

@router.put("/prods/{prod_id}", status_code=status.HTTP_204_NO_CONTENT)
async def atualizar_prod(prod_id: int,prod: ProdutoCreate, db: AsyncSession = Depends(get_db)):
    query  = select(Produto).filter(Produto.id == prod_id)
    res = await db.execute(query)
    prod_up = res.scalars().one_or_none()

    if not prod_up:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )

    if prod.nome is not None:
        prod_up.nome = prod.nome
    if prod.preco is not None:
        prod_up.preco = prod.preco
    if prod.quantidade is not None:
        prod_up.quantidade = prod.quantidade
    if prod.promocao is not None:
        prod_up.promocao = prod.promocao

    await db.commit()
    await db.refresh(prod_up)

    return prod_up

@router.delete("/prods/{prod_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_prod(prod_id: int, db: AsyncSession = Depends(get_db)):
    query  = select(Produto).filter(Produto.id == prod_id)
    res = await db.execute(query)
    prod_del = res.scalars().one_or_none()
    
    if not prod_del:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    
    await db.delete(prod_del)
    await db.commit()