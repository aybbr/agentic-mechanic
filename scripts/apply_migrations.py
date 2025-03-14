#!/usr/bin/env python
"""
Script to apply Alembic migrations.
"""
import os
import sys
import argparse
import subprocess

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


def apply_migrations(revision: str = "head") -> None:
    """Apply Alembic migrations."""
    try:
        # Run Alembic command
        subprocess.run(
            ["alembic", "upgrade", revision],
            check=True,
        )
        print(f"Migrations applied successfully to revision: {revision}")
    except Exception as e:
        print(f"Error applying migrations: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apply Alembic migrations")
    parser.add_argument(
        "--revision",
        type=str,
        default="head",
        help="Revision to upgrade to (default: head)",
    )

    args = parser.parse_args()
    apply_migrations(args.revision)
