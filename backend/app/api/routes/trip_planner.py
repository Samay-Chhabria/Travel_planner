from fastapi import APIRouter

from app.core.logging import get_logger
from app.schemas.trip_plan import TripPlanRequest, TripPlanResponse
from app.services.trip_planner_service import generate_trip_plan
from app.utils.response_utils import success_response

router = APIRouter(prefix="/trip-planner", tags=["Trip Planner"])
logger = get_logger(__name__)


@router.post("/generate", response_model=TripPlanResponse)
async def generate_plan(request: TripPlanRequest):
    """Generate a rule-based trip plan for a destination."""
    logger.info(
        "POST /trip-planner/generate destination='%s' start=%s end=%s style=%s budget=%s group=%s",
        request.destination, request.start_date, request.end_date,
        request.travel_style, request.budget_level, request.group_type,
    )

    plan = await generate_trip_plan(request)

    return success_response(
        data={"plan": plan.model_dump()},
        message="Trip plan generated successfully",
    )
