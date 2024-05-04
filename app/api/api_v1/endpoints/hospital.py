from fastapi import APIRouter, Query
from typing import List

import pandas as pd

file_path = 'datas/1.병원정보서비스.xlsx'

df = pd.read_excel(file_path)

df.rename(columns={
    '암호화요양기호': 'encrypt',
    '요양기관명': 'name',
    '종별코드': 'type_code',
    '종별코드명': 'type_name',
    '시도코드': 'city_code',
    '시도코드명': 'city_name',
    '시군구코드': 'district_code',
    '시군구코드명': 'district_name',
    '읍면동': 'town',
    '우편번호': 'zip_code',
    '주소': 'address',
    '전화번호': 'phone',
    '병원홈페이지': 'homepage',
    '개설일자': 'open_date',
    '총의사수': 'total_doctor',
    '의과일반의': 'general_doctor',
    '인원수': 'general_doctor_count',
    '의과인턴': 'intern_doctor',
    '인원수': 'intern_doctor_count',
    '의과레지던트': 'resident_doctor',
    '인원수': 'resident_doctor_count',
    '의과전문의': 'specialist_doctor',
    '인원수': 'specialist_doctor_count',
    '치과일반의': 'general_dentist',
    '인원수': 'general_dentist_count',
    '치과인턴': 'intern_dentist',
    '인원수': 'intern_dentist_count',
    '치과레지던트': 'resident_dentist',
    '인원수': 'resident_dentist_count',
    '치과전문의': 'specialist_dentist',
    '인원수': 'specialist_dentist_count',
    '한방일반의': 'general_oriental',
    '인원수': 'general_oriental_count',
    '한방인턴': 'intern_oriental',
    '인원수': 'intern_oriental_count',
    '한방레지던트': 'resident_oriental',
    '인원수': 'resident_oriental_count',
    '한방전문의': 'specialist_oriental',
    '인원수': 'specialist_oriental_count',
    '조산사': 'midwife',
    '인원수': 'midwife_count',
    '좌표(X)': 'x',
    '좌표(Y)': 'y',
}, inplace=True)

router = APIRouter()

@router.get(
    "/hospital",
    tags=["병원 조회"],
    summary="병원 정보 조회",
    description="병원 정보를 조회합니다",
    response_model=List[dict])
async def read_items(
        page: int = Query(1, ge=1),
        limit: int = Query(30, ge=1)):
    start = (page - 1) * limit
    end = start + limit
    page_data = df.iloc[start:end]
    return page_data.to_dict(orient='records')