from fastapi import Query, APIRouter
import httpx
import pandas as pd

router = APIRouter()

base_url = "https://api.odcloud.kr/api/3077892/v1/uddi:5d98d940-9da2-4abb-a809-944f85be0941"
default_page = 1
default_per_page = 100000
service_key = "oZvhlfaeFFVvLXSImE%2BrhvBcuoKoez32dWOOrCR8lvzhdi4VTnJZ8lUBq8LMdVT6%2FgLK%2FOHihCDjKiR0xWyR5A%3D%3D"

API_URL = f"{base_url}?page={default_page}&perPage={default_per_page}&serviceKey={service_key}"

file_path_name_yongsan = 'datas/서울특별시 용산구 외국어 가능 의료기관 및 약국 명단.xlsx'


@router.get("/get-yongsan-open-api/",
            tags=["공공데이터"],
            summary="서울특별시 용산구 외국어 가능 의료기관 및 약국 명단",
            description="서울특별시 용산구의 외국어 가능 의료기관 및 약국명단을 조회한다")
async def get_data(
        page: int = Query(1, description="페이지 번호"),
        perPage: int = Query(100000, description="페이지 당 항목 수")
):
    async with httpx.AsyncClient() as client:
        params = {
            "page": page,
            "perPage": perPage
        }
        response = await client.get(API_URL, params=params)
        data = response.json()

        if data['data']:
            df = pd.DataFrame(data['data'])
            # 엑셀 파일로 저장
            df.to_excel(file_path_name_yongsan, index=False)

        return data  # 반환하기 전에 파일 작업 완료
