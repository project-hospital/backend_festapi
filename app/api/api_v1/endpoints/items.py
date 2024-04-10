from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    title: str
    description: str

# 임시 아이템 데이터
fake_items_db = [{"id": 1, "title": "Football", "description": "A football"}, {"id": 2, "title": "Watch", "description": "A wrist watch"}]

router = APIRouter()

@router.get("/items", response_model=List[Item])
async def read_items():
    return fake_items_db
