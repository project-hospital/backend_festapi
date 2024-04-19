from fastapi import APIRouter, Query
from typing import List

import pandas as pd

file_path = 'datas/2.약국정보서비스.xlsx'

df = pd.read_excel(file_path)

df.rename(columns={
    '암호화요양기호': 'encrypt',
    '요양기관명': 'companyName',
    '종별코드': 'typeCode',
    '종별코드명': 'typeName',
    '시도코드': 'cityCode',
    '시도코드명': 'cityName',
    '시군구코드': 'districtCode',
    '시군구코드명': 'districtName',
    '읍면동': 'town',
    '우편번호': 'zipCode',
    '주소': 'address',
    '전화번호': 'phone',
    '개설일자': 'openDate',
    '좌표(x)': 'x',
    '좌표(y)': 'y'
}, inplace=True)

router = APIRouter()

@router.get(
    "/medicine",
    response_model=List[dict])
async def read_items(
        page: int = Query(1, ge=1),
        limit: int = Query(30, ge=1)):
    start = (page - 1) * limit
    end = start + limit
    page_data = df.iloc[start:end]
    return page_data.to_dict(orient='records')