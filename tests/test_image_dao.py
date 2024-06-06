# tests/test_image_dao.py
import pytest
from unittest.mock import AsyncMock, MagicMock
from app.api_v1.image.domain.model.image.ImageModel import Image
from app.api_v1.image.dao.image_dao import ImageDao


@pytest.mark.asyncio
async def test_create_image():
    # Mock AsyncSession
    mock_session = AsyncMock()

    # Create an instance of ImageDao with the mocked session
    image_dao = ImageDao(mock_session)

    # Define the input data
    filename = "test_image.jpg"
    url = "http://example.com/test_image.jpg"
    description = "A test image"
    file_extension = "jpg"
    create_time = "2024-05-19T00:00:00"

    # Mock the behavior of db_session.add and db_session.commit
    mock_session.add = MagicMock()
    mock_session.commit = AsyncMock()
    mock_session.refresh = AsyncMock()

    # Call the create_image method
    new_image = await image_dao.create_image(
        filename=filename,
        url=url,
        description=description,
        file_extension=file_extension,
        create_time=create_time
    )

    # Assertions
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(new_image)

    assert new_image.filename == filename
    assert new_image.url == url
    assert new_image.description == description
    assert new_image.file_extension == file_extension
    assert new_image.create_time == create_time
