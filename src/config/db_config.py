from pathlib import Path
from os import getenv
from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    db_prefix:str = "postgresql+asyncpg"
    db_url:str = f"{db_prefix}://{getenv('DB_USER','user')}:{getenv('DB_PASSWORD','password')}@{getenv('DB_HOST','localhost')}:{getenv('DB_PORT','5432')}/{getenv('DB_NAME','database')}"
    echo:bool = False

settings = Settings()