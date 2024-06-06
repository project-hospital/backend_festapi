import os

from fastapi import APIRouter, File, UploadFile, Depends

from app.api_v1.image.domain.schema.image.ImageSchema import ImageSchema
from app.api_v1.image.domain.model.image.ImageModel import Image
from app.api_v1.image.service.Image.image_service import ImageService
from app.configs.databaseConfig import get_db_session

router = APIRouter(
    prefix="/images",
    tags=["이미지 관리"])


@router.post(
    path="",
    tags=["이미지 업로드"],
    summary="이미지 업로드",
    description="이미지를 업로드하고 저장합니다",
    response_model=ImageSchema)
async def uploadImage(
        db_session=Depends(get_db_session),
        file: UploadFile = File(...),
        description: str = "이미지 설명") -> ImageSchema:

    upload_dir = "assets/uploadImages"

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    image = await Image.from_upload_file(file, upload_dir, description)
    image_service = ImageService(db_session=db_session)
    created_image = await image_service.create_image(image)

    return created_image


@router.get(
    "/downloads/{image_id}",
    tags=["이미지 다운로드"],
    summary="이미지 다운로드",
    description="이미지를 다운로드합니다",
    response_model=ImageSchema)
async def downloadImage(image_id: str):

    return await ImageService().get_image_by_id(image_id)


@router.get(
    path="",
    tags=["이미지 목록 전체조회"],
    summary="이미지 목록 전체조회",
    description="모든 이미지 목록을 조회합니다",
    response_model=list[ImageSchema])
async def getImagesAll(db_session=Depends(get_db_session)):

    return await ImageService(db_session=db_session).get_all_images()


@router.delete(
    "/{image_id}",
    tags=["이미지 삭제"],
    summary="이미지 삭제",
    description="이미지를 삭제합니다",
    response_model=bool)
async def deleteImage(
        image_id: str,
        db_session=Depends(get_db_session)):

    return await ImageService(db_session=db_session).delete_image(image_id);
