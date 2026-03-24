import pytest
from unittest.mock import AsyncMock
from src.application.use_case.post import (
    CreatePostUseCase,
    UpdatePostUseCase,
)
from src.application.dto.post import (
    PostCreateDTO,
    PostUpdateDTO,
)
from src.core.models import Post


@pytest.fixture
def mock_repo():
    mock_repo=AsyncMock()
    return mock_repo

class TestUseCase:
    
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "input_title, input_content, input_author_id, expected_id, expected_title, expected_content, expected_author_id",
        [
            ("Title 1", "Content 1", 10, 1, "Title 1", "Content 1", 10),
            ("Title 2", "Content 2", 20, 2, "Title 2", "Content 2", 20),
        ]
    )
    async def test_create_post_success(
        self, mock_repo, input_title, input_content,
        input_author_id, expected_id, expected_title,
        expected_content, expected_author_id):

        expected_post=Post(id=expected_id, title=expected_title, content=expected_content, author_id=expected_author_id)
        mock_repo.create_post.return_value=expected_post

        use_case=CreatePostUseCase(post_repo=mock_repo)

        dto=PostCreateDTO(title=input_title, content=input_content, author_id=input_author_id)
        
        result= await use_case.execute(dto)
        
        assert result.title == expected_title
        assert result.id == expected_id

        mock_repo.create_post.assert_called_once()

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "input_id, input_title, input_content, input_author_id, expected_title, expected_author_id",
        [
            (1, "New Title 1", "New Content 1", 5, "New Title 1", 5),
            (2, "New Title 2", "New Content 2", 6, "New Title 2", 6),
        ]
    )
    async def test_update_post_success(
        self, mock_repo, input_id, input_title, 
        input_content, input_author_id, expected_title,
        expected_author_id):
        expected_post=Post(id=input_id, title=expected_title, content=input_content, author_id=expected_author_id)
        mock_repo.update_post.return_value=expected_post

        use_case=UpdatePostUseCase(post_repo=mock_repo)
        dto=PostUpdateDTO(id=input_id, title=input_title, content=input_content, author_id=input_author_id)
        result=await use_case.execute(dto)

        assert result.title == expected_title
        assert result.author_id == expected_author_id
        
        mock_repo.update_post.assert_called_once()

