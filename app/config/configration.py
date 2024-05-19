from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://admin_user:qwert1234@localhost/hospital"
    host: str = "0.0.0.0"
    port: int = 5432

    class Config:
        env_file = "../.env"


settings = Settings()

__all__ = ["Settings", "settings"]
