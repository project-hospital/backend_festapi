import os
from typing import List, Optional
from app.api_v1.image.dao.image_dao import ImageDao
from app.api_v1.image.domain.model.image.ImageModel import Image
from sqlalchemy.ext.asyncio import AsyncSession

from app.api_v1.image.domain.schema.image import ImageSchema


class ImageService:
    def __init__(self, db_session: AsyncSession):
        self.image_dao = ImageDao(db_session)

    async def create_image(self, image: Image) -> ImageSchema:
        created_image = await self.image_dao.create_image(image)
        return created_image.to_schema()

    async def get_image_by_id(self, image_id: int) -> Optional[Image]:
        return await self.image_dao.get_image_by_id(image_id)

    async def get_all_images(self) -> List[Image]:
        return await self.image_dao.get_all_images()

    async def delete_image(self, image_id: int) -> bool:
        return await self.image_dao.delete_image(image_id)

    async def deleteFileAndTableDate(self, image_id: int):
        image = await self.get_image_by_id(image_id)
        if image is None:
            raise ValueError(f"Image with id {image_id} not found")
        await Image.from_delete_file(image.url)
        return await self.delete_image(image_id)
