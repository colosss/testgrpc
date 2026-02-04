from pathlib import Path
from os import getenv
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PORT = getenv('DB_PORT','5432')
DB_HOST = getenv('DB_HOST','localhost')
DB_USER = getenv('DB_USER','user')
DB_PASSWORD = getenv('DB_PASSWORD','password')
DB_NAME = getenv('DB_NAME','database')

class Settings(BaseSettings):
    db_prefix:str = "postgresql+asyncpg"
    db_url:str = f"{db_prefix}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    echo:bool = False

settings = Settings()