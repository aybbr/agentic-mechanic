import os
from pydantic_settings import BaseSettings
from typing import List, Optional, Dict, Any
from pydantic import field_validator


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

    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # Security settings
    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", "http://localhost:3000")

    @field_validator("CORS_ORIGINS")
    def validate_cors_origins(cls, v: str, info: Any) -> str:
        if v == "*" and os.getenv("ENVIRONMENT", "development") != "development":
            raise ValueError("Wildcard CORS origin (*) not allowed in production")
        return v

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
        "extra": "ignore"  # Allow extra fields in environment variables
    }


settings = Settings()
