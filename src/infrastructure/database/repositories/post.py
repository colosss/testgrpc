from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from src.core.models import Post
from src.core.repositories import AbstractPostRepository
from typing import List, Optional
from src.interfaces.grpc.post_client import run as client_run
import asyncio
import logging

class PostRepository(AbstractPostRepository):
    def __init__(self, session: AsyncSession):
        self.session=session
    
    async def get_post_by_id(self, post_id: int) -> Optional[Post]:
        post=await self.session.get(Post, post_id)
        return post
    
    async def list_posts(self, start: Optional[int] = None, end: Optional[int] = None) -> List[Post]:
        stmt=select(Post)
        if start is not None:
            stmt = stmt.offset(start)
        if end is not None:
            stmt = stmt.limit(end - start)
        result=await self.session.execute(stmt)
        post=result.scalars().all()
        return list(post)
    
    async def get_count_posts(self)->int:
        stmt=select(func.count()).select_from(Post)
        result=await self.session.execute(stmt)
        count=result.scalar_one()
        return count
    
    async def create_post(self, post:Post)->Post:
        self.session.add(post)
        await self.session.commit()
        await self.session.refresh(post)
        return post
    
    async def update_post(self, post:Post)->Post:
        db_post=await self.get_post_by_id(post.id)

        if db_post:
            db_post.title=post.title
            db_post.content=post.content
            db_post.author_id=post.author_id

            await self.session.commit()
            await self.session.refresh(db_post)
        return db_post
    
    async def delete_post(self, post_id: int) -> None:
        post=await self.get_post_by_id(post_id)
        if post:
            await self.session.delete(post)
            await self.session.commit()
        return
    
    async def get_user_by_post_id_grpc(self, post_id) -> int:
        grpc_message= await client_run(post_id)
        # db_post=await self.get_post_by_id(post_id)
        # author_id=db_post.author_id
        author_id=grpc_message
        return author_id
    
    async def get_title_by_post_id_grpc(self, post_id) -> int:
       db_post=await self.get_post_by_id(post_id)
       title=db_post.title
       return title