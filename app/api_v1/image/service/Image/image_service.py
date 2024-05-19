from typing import List, Optional
from app.api_v1.image.dao.image_dao import ImageDao
from app.api_v1.image.domain.model.image.ImageModel import Image
from sqlalchemy.ext.asyncio import AsyncSession

class ImageService:
    def __init__(self, db_session: AsyncSession):
        self.image_dao = ImageDao(db_session)

    async def create_image(self, filename: str, url: str, description: Optional[str] = None) -> Image:
        return await self.image_dao.create_image(filename, url, description)

    async def get_image_by_id(self, image_id: int) -> Optional[Image]:
        return await self.image_dao.get_image_by_id(image_id)

    async def get_all_images(self) -> List[Image]:
        return await self.image_dao.get_all_images()

    async def update_image(self, image_id: int, filename: Optional[str] = None, url: Optional[str] = None,
                           description: Optional[str] = None) -> Optional[Image]:
        return await self.image_dao.update_image(image_id, filename, url, description)

    async def delete_image(self, image_id: int) -> bool:
        return await self.image_dao.delete_image(image_id)