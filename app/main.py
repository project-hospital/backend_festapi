from fastapi import FastAPI
from app.api.api_v1.endpoints import users, hospital, medicine, image
from app.api.api_v1.endpoints.getOpenApiData import router as openapi_router
from app.config.databaseConfig import database, engine, Base
from app.config.configration import settings  # <- settings를 올바르게 가져옵니다


app = FastAPI()

app.include_router(users.router)
app.include_router(hospital.router)
app.include_router(medicine.router)
app.include_router(openapi_router)
app.include_router(image.router)

@app.on_event("startup")
async def startup():
    await database.connect()
    async with engine.begin() as conn:
        # 여기서 필요한 경우 테이블 생성 등을 수행합니다.
        # await conn.run_sync(Base.metadata.create_all)
        pass

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
