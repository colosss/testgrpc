from src.core.models import Post
from src.core.repositories import AbstractPostRepository
from src.application.dto.post import PostCreateDTO, PostDeleteDTO, PostByIdDTO, PostListDTO, PostUpdateDTO

class CreatePostUseCase:
    def __init__(self, post_repo: AbstractPostRepository) ->Post:
        self._post_repo=post_repo
    
    async def execute(self, post_dto:PostCreateDTO):
        post=Post(
            title=post_dto.title,
            content=post_dto.content,
            author_id=post_dto.author_id
        )
        created_post=await self._post_repo.create_post(post)

        return created_post

class UpdatePostUseCase:
    def __init__(self, post_repo:AbstractPostRepository)->Post:
        self._post_repo=post_repo

    async def execute(self, post_dto:PostUpdateDTO):

        post=Post(
            id=post_dto.id,
            title=post_dto.title,
            content=post_dto.content,
            author_id=post_dto.author_id
        )
        updated_post=await self._post_repo.update_post(post)

        return updated_post

class GetPostByIdUseCase:
    def __init__(self, post_repo:AbstractPostRepository):
        self._post_repo=post_repo
    
    async def execute(self, post_dto:PostByIdDTO):
        post_id=post_dto.id
        post=await self._post_repo.get_post_by_id(post_id)
        return post

class GetListPostsUseCase:
    def __init__(self, post_repo:AbstractPostRepository):
        self._post_repo=post_repo
    
    async def execute(self, post_dto:PostListDTO):
        post_list = [post_dto.start, post_dto.end]
        if all(post_list):
            posts=await self._post_repo.list_posts(post_list[0], post_list[1])
        else:
            posts=await self._post_repo.list_posts()

        return posts
    
class GetCountPostsUseCase:
    def __init__(self, post_repo:AbstractPostRepository):
        self._post_repo=post_repo
    
    async def execute(self):
        posts_count=await self._post_repo.get_count_posts()
        return posts_count

class DeletePostUseCase:
    def __init__(self, post_repo:AbstractPostRepository):
        self._post_repo=post_repo
    
    async def execute(self, post_dto:PostDeleteDTO):
        post_id=post_dto.post_id
        return await self._post_repo.delete_post(post_id)