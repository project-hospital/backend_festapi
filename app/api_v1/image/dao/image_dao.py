from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.api_v1.image.domain.model.image.ImageModel import Image
from typing import List, Optional


class ImageDao:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_image(self, filename: str, url: str, description: Optional[str] = None) -> Image:
        new_image = Image(filename=filename, url=url, description=description)
        self.db_session.add(new_image)
        await self.db_session.commit()
        await self.db_session.refresh(new_image)
        return new_image

    async def get_image_by_id(self, image_id: int) -> Optional[Image]:
        result = await self.db_session.execute(select(Image).filter(Image.id == image_id))
        return result.scalars().first()

    async def get_all_images(self) -> List[Image]:
        result = await self.db_session.execute(select(Image))
        return result.scalars().all()

    async def update_image(self, image_id: int, filename: Optional[str] = None, url: Optional[str] = None,
                           description: Optional[str] = None) -> Optional[Image]:
        update_stmt = (
            update(Image)
            .where(Image.id == image_id)
            .values(filename=filename, url=url, description=description)
            .execution_options(synchronize_session="fetch")
        )
        await self.db_session.execute(update_stmt)
        await self.db_session.commit()
        return await self.get_image_by_id(image_id)

    async def delete_image(self, image_id: int) -> bool:
        delete_stmt = delete(Image).where(Image.id == image_id)
        await self.db_session.execute(delete_stmt)
        await self.db_session.commit()
        return True
