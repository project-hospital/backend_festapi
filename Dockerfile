# Python 3.9 공식 이미지를 기반으로 설정
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt ./

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드를 컨테이너로 복사
COPY ./app ./app

# datas 폴더를 컨테이너로 복사
COPY ./datas ./datas

# Uvicorn으로 FastAPI 애플리케이션 실행, 경로 수정
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
