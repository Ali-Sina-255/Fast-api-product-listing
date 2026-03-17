from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict  # type: ignore

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Setting(BaseSettings):
    # =========================
    # ENVIRONMENT
    # =========================
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".envs/.env.local",
        env_ignore_empty=True,
        extra="ignore",
    )

    # =========================
    # PROJECT INFO
    # =========================
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "My FastAPI Project"
    PROJECT_DESCRIPTION: str = "API for managing products"
    SITE_NAME: str = "MySite"

    # =========================
    # DATABASE
    # =========================
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "test_db"

    # =========================
    # EMAIL
    # =========================
    MAIL_FROM: str = ""
    MAIL_FROM_NAME: str = ""
    SMTP_HOST: str = ""
    SMTP_PORT: int = 1025
    MAILPIT_UI_PORT: int = 8025

    # =========================
    # REDIS
    # =========================
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    # =========================
    # RABBITMQ
    # =========================
    RABBITMQ_HOST: str = "localhost"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USER: str = "guest"
    RABBITMQ_PASSWORD: str = "guest"

    # =========================
    # DATABASE URL
    # =========================
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}"
            f"/{self.POSTGRES_DB}"
        )


settings = Setting()
