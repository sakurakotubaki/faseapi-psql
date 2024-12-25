from pydantic_settings import BaseSettings
from typing import Optional
from datetime import datetime
import pytz

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Auth API"
    SECRET_KEY: str = "your-secret-key-here"  # 本番環境では必ず変更してください
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "postgresql://wakuwaku:1234qq@db:5432/auth_db"

    # Database settings
    POSTGRES_USER: str = "wakuwaku"
    POSTGRES_PASSWORD: str = "1234qq"
    POSTGRES_DB: str = "auth_db"
    TZ: str = "Asia/Tokyo"

    @staticmethod
    def get_current_time() -> str:
        return datetime.now(pytz.timezone('Asia/Tokyo')).isoformat()

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
