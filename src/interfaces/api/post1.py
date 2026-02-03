from fastapi import APIRouter, Depends
from typing import List

from src.application.use_case.post import (
    CreatePostUseCase,
    GetListPostsUseCase,
    GetPostByIdUseCase,
    UpdatePostUseCase,
    DeletePostUseCase,
)
from src.application.dto.post import (
    PostCreateDTO,
    PostListDTO,
    PostByIdDTO,
    PostUpdateDTO,
    PostDeleteDTO,
)
from src.core.models import Post
from src.infrastructure.database.db_helper import db_helper
from src.infrastructure.database.repositories.post import PostRepository

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/", response_model=Post)
async def create_post(
    post_dto: PostCreateDTO,
    post_repo: PostRepository = Depends(db_helper.get_post_repo),
):
    use_case = CreatePostUseCase(post_repo)
    return await use_case.execute(post_dto)


@router.get("/", response_model=List[Post])
async def get_all_posts(
    start: int = 0,
    end: int = 10,
    post_repo: PostRepository = Depends(db_helper.get_post_repo),
):
    use_case = GetListPostsUseCase(post_repo)
    return await use_case.execute(PostListDTO(start=start, end=end))


@router.get("/{post_id}", response_model=Post)
async def get_post_by_id(
    post_id: int,
    post_repo: PostRepository = Depends(db_helper.get_post_repo),
):
    use_case = GetPostByIdUseCase(post_repo)
    return await use_case.execute(PostByIdDTO(id=post_id))


@router.put("/{post_id}", response_model=Post)
async def update_post(
    post_id: int,
    post_dto: PostUpdateDTO,
    post_repo: PostRepository = Depends(db_helper.get_post_repo),
):
    post_dto.id = post_id
    use_case = UpdatePostUseCase(post_repo)
    return await use_case.execute(post_dto)


@router.delete("/{post_id}", status_code=204)
async def delete_post(
    post_id: int,
    post_repo: PostRepository = Depends(db_helper.get_post_repo),
):
    use_case = DeletePostUseCase(post_repo)
    return await use_case.execute(PostDeleteDTO(post_id=post_id))
