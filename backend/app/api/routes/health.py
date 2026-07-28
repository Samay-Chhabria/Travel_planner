from fastapi import APIRouter

from app.core.config import get_settings
from app.core.logging import get_logger
from app.utils.response_utils import success_response

logger = get_logger(__name__)
router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check():
    """Return service health status."""
    settings = get_settings()
    logger.debug("Health check requested")
    return success_response(
        data={
            "status": "ok",
            "service": settings.SERVICE_NAME,
            "version": settings.API_VERSION,
        },
        message="Service is healthy",
    )
