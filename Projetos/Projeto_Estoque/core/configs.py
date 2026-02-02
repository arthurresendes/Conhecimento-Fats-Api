from typing import Any, ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "sqlite+aiosqlite:///./estoque.db"
    DBBaseModel: ClassVar[Any] = declarative_base()
    
    JWT_SECRET: str = "ep771f7fsZIDxbNvDFkJxvh8DB_QMsFBfryyqx-rDZs"

    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True

settings: Settings = Settings()