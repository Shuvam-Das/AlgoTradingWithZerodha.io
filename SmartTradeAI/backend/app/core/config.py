import os
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "SmartTradeAI"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, List):
            return v
        raise ValueError(v)

    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

    SQLALCHEMY_DATABASE_URI: Optional[str] = os.getenv("DATABASE_URL")

    FIRST_SUPERUSER_EMAIL: EmailStr = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
