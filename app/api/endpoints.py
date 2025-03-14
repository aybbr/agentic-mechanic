from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to Agentic Mechanic API"}
