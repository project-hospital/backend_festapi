from uuid import UUID

from pydantic import BaseModel
from typing import Optional


class ImageSchema(BaseModel):
    id: UUID
    filename: str
    url: str
    description: Optional[str] = None
    file_extension: Optional[str] = None
    create_time: Optional[str] = None

    class Config:
        orm_mode = True
