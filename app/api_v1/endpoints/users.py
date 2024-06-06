from fastapi import APIRouter
from typing import List
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int


# 임시 사용자 데이터
fake_users_db = [
    {
        "id": 1,
        "name": "Alice",
        "age": 25
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 30
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 35
    }
]

router = APIRouter()


@router.get("/users", response_model=List[User])
async def read_users():
    return fake_users_db
