from pydantic import BaseModel
from typing import Union


class ImageBase(BaseModel):
    filename: str
    url: str
    description: Union[str, None] = None


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int

    class Config:
        orm_mode = True
