# Agentic Mechanic API

A production-grade FastAPI application with modern architecture and best practices, designed for deployment on Vercel.

## Features

- **Modern Python**: Fully typed with Python 3.13
- **FastAPI Framework**: High performance, easy to learn, fast to code
- **Supabase Integration**: PostgreSQL database with Supabase
- **Authentication**: JWT token-based authentication with PyJWT
- **Dependency Injection**: Clean service-based architecture
- **Pydantic Models**: Request and response validation
- **Error Handling**: Centralized error handling with custom exceptions
- **Testing**: Pytest setup for unit, integration, and e2e tests
- **Vercel Ready**: Optimized for serverless deployment on Vercel
- **Database Migrations**: Alembic for managing database schema changes

## Project Structure

```
/
├── api/                    # Vercel serverless functions
│   └── index.py            # Main entry point for Vercel
├── app/                    # Main application code
│   ├── api/                # API route handlers and errors
│   ├── core/               # Core application code
│   ├── db/                 # Database models and session
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   └── services/           # Business logic
├── alembic/                # Database migration scripts
├── scripts/                # Utility scripts
├── tests/                  # Test directory
├── alembic.ini             # Alembic configuration
├── requirements.txt        # Python dependencies
├── run.py                  # Local development server
└── vercel.json             # Vercel configuration
```

## Getting Started

### Prerequisites

- Python 3.13+
- Supabase account

### Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv3am
   source venv3am/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up environment variables (copy `.env.example` to `.env` and modify as needed)

### Running the Application Locally

```
python run.py
```

The API will be available at http://localhost:8000

API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Database Migrations with Alembic

This project uses Alembic to manage database schema changes. Here's how to use it:

### Creating a New Migration

After making changes to your SQLAlchemy models, create a new migration:

```
python scripts/create_migration.py "description of changes"
```

### Applying Migrations

To apply all pending migrations:

```
python scripts/apply_migrations.py
```

To apply migrations up to a specific revision:

```
python scripts/apply_migrations.py --revision revision_id
```

### Reverting Migrations

To revert to a previous migration:

```
alembic downgrade revision_id
```

## Deployment to Vercel

This project is configured for deployment on Vercel. To deploy:

1. Push your code to a Git repository
2. Connect the repository to Vercel
3. Configure environment variables in Vercel dashboard
4. Deploy!

## Development

### Running Tests

```
pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
