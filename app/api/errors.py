from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class AppException(Exception):
    """Base exception class for application-specific exceptions."""
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail


async def app_exception_handler(request: Request, exc: AppException):
    """Handler for application-specific exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


def register_exception_handlers(app: FastAPI):
    """Register all exception handlers with the FastAPI application."""
    app.add_exception_handler(AppException, app_exception_handler)
