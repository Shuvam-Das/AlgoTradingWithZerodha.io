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

    # Zerodha Kite API
    KITE_API_KEY: str = os.getenv("KITE_API_KEY", "your-kite-api-key")
    KITE_API_SECRET: str = os.getenv("KITE_API_SECRET", "your-kite-api-secret")
    KITE_ACCESS_TOKEN: str = os.getenv("KITE_ACCESS_TOKEN", "your-kite-access-token")

    # NewsAPI
    NEWS_API_KEY: str = os.getenv("NEWS_API_KEY", "your-news-api-key")

    # OpenAI API
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "your-openai-api-key")

    # Telegram Bot
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "your-telegram-bot-token")

    # Celery
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

    # Celery
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
