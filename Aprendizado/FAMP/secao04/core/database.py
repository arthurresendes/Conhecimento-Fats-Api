from sqlalchemy.orm import sessionmaker # Cria a fabrica de seções ond enela sera possivel interagir com banco de dados
from sqlalchemy.ext.asyncio import create_async_engine,AsyncEngine,AsyncSession # Criação da estrtura do banco de dados que vem do seetings com Estruturas e sessões assincronicas 
from core.configs import settings


engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)