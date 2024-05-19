# app/api_v1/image/domain/model/image/ImageSchema.py
from pydantic import BaseModel
from typing import Optional


class ImageSchema(BaseModel):
    id: Optional[int]
    filename: str
    url: str
    description: Optional[str] = None
    file_extension: Optional[str] = None
    create_time: Optional[str] = None

    class Config:
        orm_mode = True
