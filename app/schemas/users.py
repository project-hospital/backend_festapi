from pydantic import BaseModel, EmailStr


# 사용자 생성을 위한 스키마
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


# 사용자 정보 조회를 위한 스키마
class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # ORM 모델과 호환되도록 설정


# 사용자 정보 업데이트를 위한 스키마
class UserUpdate(BaseModel):
    name: str = None
    email: EmailStr = None
    password: str = None
