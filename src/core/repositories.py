from abc import ABC, abstractmethod
from typing import List,Optional
from src.core.models import Post

class AbstractPostRepository(ABC):

    @abstractmethod
    async def get_post_by_id(self, post_id:int)->Optional[Post]:
        pass

    @abstractmethod
    async def list_posts(self, start:Optional[int], end:Optional[int])->List[Post]:
        pass

    @abstractmethod
    async def get_count_posts(self)->int:
        pass

    @abstractmethod
    async def create_post(self, post:Post)->Post:
        pass

    @abstractmethod
    async def update_post(self, post:Post)->Post:
        pass

    @abstractmethod
    async def delete_post(self, post_id:int)->None:
        pass

    