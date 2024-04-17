from fastapi import APIRouter, Query
from typing import List
from pydantic import BaseModel

import pandas as pd
import io

# Excel 파일 경로
file_path = 'datas/1.병원정보서비스.xlsx'

# Excel 파일 읽기
df = pd.read_excel(file_path)

router = APIRouter()

@router.get("/hospital", response_model=List[dict])
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