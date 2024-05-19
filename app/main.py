from fastapi import FastAPI
from app.api.api_v1.endpoints import users, hospital, medicine, imageController
from app.api.api_v1.endpoints.getOpenApiData import router as openapi_router
from app.config.databaseConfig import database, engine, Base
from app.api.api_v1.domain.model.image.ImageModel import Image


app = FastAPI()

app.include_router(users.router)
app.include_router(hospital.router)
app.include_router(medicine.router)
app.include_router(openapi_router)
app.include_router(imageController.router)

@app.on_event("startup")
async def startup():
    await database.connect()
    async with engine.begin() as conn:
        # 필요한 경우 테이블을 생성합니다.
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
