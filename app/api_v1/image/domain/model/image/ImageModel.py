import os
import uuid
from datetime import datetime

import aiofiles
from fastapi import UploadFile
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID

from app.api_v1.image.domain.schema.image.ImageSchema import ImageSchema
from app.configs.databaseConfig import Base


class Image(Base):
    __tablename__ = 'image'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    filename = Column(String, index=True, nullable=False)  # unique=True 제거
    url = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    file_extension = Column(String, nullable=True)
    create_time = Column(String, nullable=True)

    def __repr__(self):
        return (f"<Image(id={self.id}, filename={self.filename}, url={self.url}, description={self.description}, "
                f"file_extension={self.file_extension}), create_time={self.create_time}>")

    @classmethod
    async def from_upload_file(cls, file: UploadFile, upload_dir: str, description: str = "이미지 설명"):
        id = uuid.uuid4()
        file_extension = file.filename.rsplit('.', 1)[-1]
        unique_filename = f"{uuid.uuid4()}-{file.filename}"  # UUID를 포함하여 고유 파일 이름 생성
        url = os.path.join(upload_dir, unique_filename)
        create_time = datetime.now().isoformat()

        async with aiofiles.open(url, "wb") as buffer:
            contents = await file.read()
            await buffer.write(contents)

        return cls(
            id=id,
            filename=file.filename,  # 원래 파일 이름 유지
            url=url,
            description=description,
            file_extension=file_extension,
            create_time=create_time
        )

    @classmethod
    async def from_delete_file(cls, url: str):
        if os.path.exists(url):
            os.remove(url)


    def to_schema(self) -> ImageSchema:
        return ImageSchema(
            id=self.id,
            filename=self.filename,
            url=self.url,
            description=self.description,
            file_extension=self.file_extension,
            create_time=self.create_time
        )
