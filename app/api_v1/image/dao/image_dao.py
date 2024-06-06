from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.api_v1.image.domain.model.image.ImageModel import Image
from typing import List, Optional


class ImageDao:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_image(self, image: Image) -> Image:
        self.db_session.add(image)
        await self.db_session.commit()
        await self.db_session.refresh(image)
        return image

    async def get_image_by_id(self, image_id: int) -> Optional[Image]:
        result = await self.db_session.execute(select(Image).filter(Image.id == image_id))
        return result.scalars().first()

    async def get_all_images(self) -> List[Image]:
        result = await self.db_session.execute(select(Image))
        return result.scalars().all()

    async def delete_image(self, image_id: int) -> bool:
        delete_stmt = delete(Image).where(Image.id == image_id)
        await self.db_session.execute(delete_stmt)
        await self.db_session.commit()
        return True
