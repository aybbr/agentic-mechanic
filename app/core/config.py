import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # Project info
    PROJECT_NAME: str = "Agentic Mechanic API"
    PROJECT_DESCRIPTION: str = "API for Agentic Mechanic"
    VERSION: str = "0.1.0"

    # API settings
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    OPENAPI_URL: str = "/openapi.json"

    # Database settings
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/agentic_mechanic")

    # JWT settings
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "supersecretkey")
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
        "extra": "ignore"  # Allow extra fields in environment variables
    }


settings = Settings()
