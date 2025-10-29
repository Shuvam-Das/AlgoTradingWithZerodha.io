from typing import Any, Dict, List, Optional
from pydantic_settings import BaseSettings
from pydantic import EmailStr, AnyHttpUrl, validator

class Settings(BaseSettings):
    PROJECT_NAME: str = "SmartTradeAI"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "AI-Powered Algorithmic Trading Platform"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"  # Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str
    
    # Redis
    REDIS_URL: str
    
    # Celery
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    
    # CORS
    ALLOWED_ORIGINS: List[AnyHttpUrl] = []
    
    # Email
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAIL_FROM: Optional[EmailStr] = None
    EMAIL_TEST_USER: EmailStr = "test@example.com"
    
    # Zerodha
    ZERODHA_API_KEY: Optional[str] = None
    ZERODHA_API_SECRET: Optional[str] = None
    
    # OpenAI
    OPENAI_API_KEY: Optional[str] = None
    
    # News API
    NEWS_API_KEY: Optional[str] = None
    
    # Telegram Bot
    TELEGRAM_BOT_TOKEN: Optional[str] = None
    
    class Config:
        case_sensitive = True
        env_file = ".env"

    @validator("ALLOWED_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

settings = Settings()