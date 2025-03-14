#!/usr/bin/env python
"""
Script to create a new Alembic migration.
"""
import os
import sys
import argparse
import subprocess

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def create_migration(message: str) -> None:
    """Create a new Alembic migration."""
    try:
        # Import models to ensure they are registered with SQLAlchemy
        from app.models import User

        # Run Alembic command
        subprocess.run(
            ["alembic", "revision", "--autogenerate", "-m", message],
            check=True,
        )
        print(f"Migration created successfully with message: {message}")
    except Exception as e:
        print(f"Error creating migration: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new Alembic migration")
    parser.add_argument(
        "message",
        type=str,
        help="Message for the migration",
    )

    args = parser.parse_args()
    create_migration(args.message)
