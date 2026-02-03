from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite+aiosqlite:///./cliente.db"

engine = create_async_engine(DB_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    engine,
    class_= AsyncSession,
    expire_on_commit = False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session