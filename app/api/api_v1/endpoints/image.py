from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel
from datetime import datetime, time
import uuid
import os

router = APIRouter()


class Image(BaseModel):
    id: str
    name: str
    path: str
    fileExtension: str
    createTime: str


@router.post(
    "/image",
    tags=["이미지 업로드"],
    summary="이미지 업로드",
    description="이미지를 업로드하고 저장합니다",
    response_model=Image)
async def uploadImage(file: UploadFile = File(...)):
    image_id = str(uuid.uuid4())
    file_extension = file.filename.rsplit('.', 1)[-1]
    upload_dir = "assets/uploadImages"
    file_path = os.path.join(upload_dir, f"{image_id}.{file_extension}")

    # 디렉토리가 없다면 생성
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # 파일을 비동기적으로 저장
    with open(file_path, "wb") as buffer:
        contents = await file.read()  # 비동기적으로 파일 읽기
        buffer.write(contents)

    # 이미지 객체 생성
    image = Image(
        id=image_id,
        name=file.filename,
        path=file_path,
        fileExtension=file_extension,
        createTime=datetime.now().isoformat()
    )

    return image
