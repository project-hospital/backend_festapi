from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel


# Pydantic 모델 정의 (요청 및 응답 스키마)
class User(BaseModel):
    id: int
    name: str
    age: int


# 임시 데이터베이스 역할을 할 리스트
fake_db = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Doe", "age": 25}
]

router = APIRouter()


# 모든 사용자 목록을 가져오는 엔드포인트
@router.get("/users", response_model=List[User])
async def read_users():
    return fake_db


# 새로운 사용자를 생성하는 엔드포인트
@router.post("/users", response_model=User)
async def create_user(user: User):
    fake_db.append(user.dict())
    return user
