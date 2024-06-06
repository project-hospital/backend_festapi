from fastapi import FastAPI
from app.api_v1.endpoints import hospital, medicine, users
from app.api_v1.image.controller import imageController
from app.api_v1.endpoints.getOpenApiData import router as openapi_router
from app.configs.databaseConfig import database, engine, Base

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users.router)
app.include_router(hospital.router)
app.include_router(medicine.router)
app.include_router(openapi_router)
app.include_router(imageController.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
