import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.infrastructure.database import db_helper
from interfaces.api import post


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(db_helper.Base.metadata.create_all)
    yield
    

app = FastAPI(lifespan=lifespan)
app.include_router(post.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
