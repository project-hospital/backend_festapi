from fastapi import Query, APIRouter
import httpx

router = APIRouter()

API_URL = ("https://api.odcloud.kr/api/3077892/v1/uddi:5d98d940-9da2-4abb-a809-944f85be0941?page=1&perPage=10"
           "&serviceKey=oZvhlfaeFFVvLXSImE%2BrhvBcuoKoez32dWOOrCR8lvzhdi4VTnJZ8lUBq8LMdVT6%2FgLK%2FOHihCDjKiR0xWyR5A"
           "%3D%3D")


@router.get("/get-yongsan-open-api/", tags=["공공데이터 포털 오픈 API"], summary="서울특별시 용산구_외국어가능의료기관및약국명단",
            description="서울특별시 용산구_외국어가능의료기관및약국명단을 조회합니다")
async def get_data(
        page: int = Query(1, description="페이지 번호"),
        perPage: int = Query(10, description="페이지 당 항목 수")
):
    async with httpx.AsyncClient() as client:
        params = {
            "page": page,
            "perPage": perPage
        }
        response = await client.get(API_URL, params=params)
        return response.json()