from fastapi import APIRouter, File, UploadFile, Depends
# from sqlalchemy.ext.asyncio import AsyncSession
from app.configs.databaseConfig import get_db_session
# from datetime import datetime
# from app.api_v1.image.domain.model.image.ImageModel import image_model
from app.api_v1.image.domain.schema.image.ImageSchema import ImageSchema
from app.api_v1.image.service.Image.image_service import ImageService

# import uuid
# import os

router = APIRouter(prefix="/images", tags=["이미지 관리"])


# @router.post(
#     "/image",
#     tags=["이미지 업로드"],
#     summary="이미지 업로드",
#     description="이미지를 업로드하고 저장합니다",
#     response_model=Image)
# async def uploadImage(file: UploadFile = File(...)):
#     image_id = str(uuid.uuid4())
#     file_extension = file.filename.rsplit('.', 1)[-1]
#     upload_dir = "assets/uploadImages"
#     file_path = os.path.join(upload_dir, f"{image_id}.{file_extension}")
#
#     # 디렉토리가 없다면 생성
#     if not os.path.exists(upload_dir):
#         os.makedirs(upload_dir)
#
#     # 파일을 비동기적으로 저장
#     with open(file_path, "wb") as buffer:
#         contents = await file.read()  # 비동기적으로 파일 읽기
#         buffer.write(contents)
#
#     # 이미지 객체 생성
#     image = Image(
#         id=image_id,
#         filename=file.filename,
#         url=file_path,
#         file_extension=file_extension,
#         createTime=datetime.now().isoformat()
#     )
#
#     ImageService().create_image(image)
#
#     return image


# @router.get(
#     "/image/{image_id}",
#     tags=["이미지 다운로드"],
#     summary="이미지 다운로드",
#     description="이미지를 다운로드합니다",
#     response_model=Image)
# async def downloadImage(image_id: str):
#     image = Image(
#         id=image_id,
#         name="sample.jpg",
#         path="assets/sample.jpg",
#         fileExtension="jpg",
#         createTime=datetime.now().isoformat()
#     )
#     return image

@router.get(
    "",
    tags=["이미지 목록 조회"],
    summary="이미지 목록 조회",
    description="모든 이미지 목록을 조회합니다",
    response_model=list[ImageSchema]
)
async def getImages(db_session=Depends(get_db_session)):
    image_service = ImageService(db_session=db_session)
    return image_service.get_all_images()

# @router.delete(
#     "/image/{image_id}",
#     tags=["이미지 삭제"],
#     summary="이미지 삭제",
#     description="이미지를 삭제합니다",
#     response_model=bool)
# async def deleteImage(image_id: str):
#     return True;
