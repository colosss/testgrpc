from sqlalchemy.orm import Mapped
from ..infreastructure.database.base import Base

class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str]
    content: Mapped[str]
    author_id: Mapped[int]