from pydantic import BaseModel
from typing import Optional, List

class PostCreateDTO(BaseModel):
    title:str
    content:str
    author_id:int

class PostUpdateDTO(BaseModel):
    id: int
    title:Optional[str]=None
    content:Optional[str]=None
    author_id:Optional[int]=None

class PostByIdDTO(BaseModel):
    id:int

class PostListDTO(BaseModel):
    start:Optional[int]=None
    end:Optional[int]=None

class PostDeleteDTO(BaseModel):
    post_id:int
