from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (  # type: ignore
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base  # type: ignore

from apps.config.config import settings
from apps.config.logging import get_logger

logger = get_logger()


# =========================
# BASE (IMPORTANT)
# =========================
Base = declarative_base()
# =========================
# ENGINE
# =========================
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,  # set True for debugging SQL
    future=True,
)

# =========================
# SESSION
# =========================
async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# =========================
# DEPENDENCY
# =========================
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Database session error: {e}")
            await session.rollback()
            raise
        finally:
            await session.close()


# =========================
# INIT DB
# =========================
async def init_db() -> None:
    try:
        from apps.config.model_registry import load_models

        load_models()
        logger.info("✅ Models loaded successfully")

    except Exception as e:
        logger.error(f"❌ Failed to load models: {e}")
