from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.logging import get_logger

logger = get_logger(__name__)


class AppError(Exception):
    """Base application error."""

    def __init__(self, code: str = "INTERNAL_ERROR", message: str = "An unexpected error occurred", status_code: int = 500):
        self.code = code
        self.message = message
        self.status_code = status_code


class NotFoundError(AppError):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(code="NOT_FOUND", message=message, status_code=404)


class UpstreamProviderError(AppError):
    def __init__(self, message: str = "External provider is temporarily unavailable"):
        super().__init__(code="UPSTREAM_PROVIDER_ERROR", message=message, status_code=502)


class ValidationError(AppError):
    def __init__(self, message: str = "Request validation failed", details: list | None = None):
        super().__init__(code="VALIDATION_ERROR", message=message, status_code=422)
        self.details = details or []


async def app_error_handler(_request: Request, exc: AppError) -> JSONResponse:
    body: dict = {"success": False, "error": {"code": exc.code, "message": exc.message}}
    if isinstance(exc, ValidationError) and exc.details:
        body["error"]["details"] = exc.details
    return JSONResponse(status_code=exc.status_code, content=body)


async def validation_error_handler(_request: Request, exc: RequestValidationError) -> JSONResponse:
    details = [
        {"field": ".".join(str(loc) for loc in err.get("loc", [])), "issue": err.get("msg", "")}
        for err in exc.errors()
    ]
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Request validation failed",
                "details": details,
            },
        },
    )


async def unhandled_error_handler(_request: Request, _exc: Exception) -> JSONResponse:
    logger.exception("Unhandled error: %s", _exc)
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {"code": "INTERNAL_ERROR", "message": "An unexpected error occurred"},
        },
    )
