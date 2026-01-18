from pydantic_settings import BaseSettings # Usado para configurações de ambiente e foi utiliza como herdeito na class Settings

from sqlalchemy.ext.declarative import declarative_base # Modelo base , todas tabelas do banco herdam daqui

from typing import ClassVar # É um atributo de classe inteira

class Setting(BaseSettings):
    """
    Configurações gerais utilizadas na aplicação
    """
    API_V1_STR:str = '/api/v1' # Caminho padrão da api v1
    DB_URL: str = "sqlite+aiosqlite:///./faculdade.db" # URL do banco de dados + aiosqlite para ser usado juntamento com funções assincronicas //./ indica que sera nesse repositorio
    DBBaseModel: ClassVar = declarative_base() # Modelo base , permitindo a definição de modelos de banco de dados
    
    class Config:
        case_sensitive = True # Diz ao Pydantic que as variáveis são sensíveis a maiúsculas/minúsculas.


settings = Setting() # Instanciando um objeto para utilizar ele