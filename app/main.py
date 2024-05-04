from fastapi import FastAPI
from app.api.api_v1.endpoints import users, hospital, medicine, image
from app.api.api_v1.endpoints.getOpenApiData import router as openapi_router
app = FastAPI()

app.include_router(users.router)
app.include_router(hospital.router)
app.include_router(medicine.router)
app.include_router(openapi_router)
app.include_router(image.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
