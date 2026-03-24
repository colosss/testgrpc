from fastapi import APIRouter, Depends, status
from typing import List, Optional

from src.application.dto.post import(
    PostSchema,
    PostDeleteDTO,
    PostByIdDTO,
    PostCreateDTO,
    PostListDTO,
    PostUpdateDTO,
    UserNameByIdGrpcDTO,
    TitleByPostIdGrpcDTO,
)

from src.application.use_case.post import (
    GetCountPostsUseCase,
    GetListPostsUseCase,
    GetPostByIdUseCase,
    CreatePostUseCase,
    UpdatePostUseCase,
    DeletePostUseCase,
    GetTitleByPoststrIdGrpcUseCase,
    GetUserNameByPostIdGrpcUseCase,
)

from src.core.models import Post
from src.infrastructure.database.base import Base
from src.infrastructure.database.db_helper import db_helper
from src.infrastructure.database.repositories.post import PostRepository

router=APIRouter(prefix="/post", tags=["Post"])
grpc=APIRouter(prefix="/grpc", tags=["gRPC"])

@router.post("/", response_model=PostSchema)
async def create_post(
    title:str=None,
    content:str=None,
    author_id:int=None,
    post_repo:PostRepository=Depends(db_helper.get_post_repo),
):
    use_case=CreatePostUseCase(post_repo)
    return await use_case.execute(PostCreateDTO(title=title, content=content, author_id=author_id))

@router.get("/", response_model=List[PostSchema])
async def get_all_posts(
    start:Optional[int]=None,
    end:Optional[int]=None,
    post_repo:PostRepository=Depends(db_helper.get_post_repo),
):
    use_case=GetListPostsUseCase(post_repo)
    return await use_case.execute(PostListDTO(start=start, end=end))

@router.get("/{post_id}", response_model=PostSchema)
async def get_post_by_id(
    post_id:int,
    post_repo:PostRepository=Depends(db_helper.get_post_repo)
):
    use_case=GetPostByIdUseCase(post_repo)
    return await use_case.execute(PostByIdDTO(id=post_id))

@router.put("/{post_id}", response_model=PostSchema)
async def update_post(
    post_id:int,
    post_dto:PostUpdateDTO,
    post_repo:PostRepository=Depends(db_helper.get_post_repo)
):
    post_dto.id=post_id
    use_case=UpdatePostUseCase(post_repo)
    return await use_case.execute(post_dto)

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post_id:int,
    post_repo:PostRepository=Depends(db_helper.get_post_repo)
):
    use_case=DeletePostUseCase(post_repo)
    return await use_case.execute(PostDeleteDTO(post_id=post_id))

# @grpc.get("/{post_id}", response_model=PostSchema)
# async def get_user_by_post_id_grpc(
#     post_id:int,
#     post_repo:PostRepository=Depends(db_helper.get_post_repo)
# ):
#     use_case=GetUserNameByPostIdGrpcUseCase(post_repo)
#     return await use_case.execute(UserNameByIdGrpcDTO(post_id=post_id))

# @grpc.get("/title/{post_id}", response_model=PostSchema)
# async def get_title_by_post_id_grpc(
#     post_id:int,
#     post_repo:PostRepository=Depends(db_helper.get_post_repo)
# ):
#     use_case=GetTitleByPoststrIdGrpcUseCase(post_repo)
#     return await use_case.execute(TitleByPostIdGrpcDTO(post_id=post_id))

@grpc.get("/{post_id}", response_model=PostSchema)
async def get_user_by_post_id_grpc(
    post_id:int
):
    use_case=GetUserNameByPostIdGrpcUseCase