"""Database initialization script."""
import logging

from sqlalchemy.orm import Session

from app.db.base import Base, engine
from app.core.config import settings

# Import all models to ensure they are registered with SQLAlchemy
from app.models import User

logger = logging.getLogger(__name__)


def init_db() -> None:
    """Initialize the database by creating all tables."""
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        raise


if __name__ == "__main__":
    init_db()
