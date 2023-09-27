from typing import Set
from pydantic_settings import BaseSettings


class EnvironmentSettings(BaseSettings):
    API_VERSION: str = "v1"
    APP_NAME: str = "HMS"
    TEST_DATABASE_URL: str = ""
    POSTGRES_DB_URL: str = "postgres://mmbdizrs:PVGxct-9uK2wXI9bucU_hqRzaSQ_B74s@salt.db.elephantsql.com/mmbdizrs"
    DEBUG_MODE: bool = False
    JWT_SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    JWT_ALGORITHM: str = "HS256"
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000","http://localhost:5174"]


settings = EnvironmentSettings()
