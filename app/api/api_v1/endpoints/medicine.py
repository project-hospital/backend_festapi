from fastapi import APIRouter, Query
from typing import List

import pandas as pd

file_path = 'datas/2.약국정보서비스.xlsx'

df = pd.read_excel(file_path)

router = APIRouter()

@router.get("/medicine", response_model=List[dict])
async def read_items(
        page: int = Query(1, ge=1),
        limit: int = Query(30, ge=1)):
    # 페이지네이션을 위한 계산
    start = (page - 1) * limit
    end = start + limit
    # 데이터 슬라이싱
    page_data = df.iloc[start:end]
    # 결과 반환
    return page_data.to_dict(orient='records')