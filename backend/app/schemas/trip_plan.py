import datetime

from pydantic import BaseModel, Field, model_validator


class TripPlanRequest(BaseModel):
    destination: str = Field(..., min_length=1, description="Destination name, e.g. Paris")
    start_date: datetime.date = Field(..., description="Trip start date (YYYY-MM-DD)")
    end_date: datetime.date = Field(..., description="Trip end date (YYYY-MM-DD)")
    travel_style: str = Field(default="general", description="Travel style: culture, adventure, food, relaxation, general")
    budget_level: str = Field(default="moderate", description="Budget tier: budget, moderate, luxury")
    group_type: str = Field(default="couple", description="Group type: solo, couple, family, friends")

    @model_validator(mode="after")
    def validate_dates(self):
        if self.end_date < self.start_date:
            raise ValueError("end_date must be after or equal to start_date")
        return self


class ActivityItem(BaseModel):
    time: str = Field(default="", description="Suggested time, e.g. 09:00")
    description: str = Field(..., description="Activity description")


class DayPlan(BaseModel):
    day: int = Field(..., description="Day number (1-indexed)")
    date: datetime.date = Field(..., description="Date in YYYY-MM-DD format")
    title: str = Field(..., description="Short day title")
    activities: list[ActivityItem] = Field(default_factory=list)
    notes: str = Field(default="", description="Travel tips for the day")


class TripPlan(BaseModel):
    id: str = Field(..., description="Unique plan identifier")
    destination: str = Field(..., description="Destination name")
    country: str = Field(default="", description="Country name")
    duration_days: int = Field(..., description="Total trip duration in days")
    travel_style: str = Field(default="general", description="Travel style used")
    budget_level: str = Field(default="moderate", description="Budget level used")
    group_type: str = Field(default="couple", description="Group type used")
    summary: str = Field(default="", description="Trip summary")
    days: list[DayPlan] = Field(default_factory=list)
    weather_summary: str = Field(default="", description="Brief weather outlook")
    top_attractions: list[str] = Field(default_factory=list, description="Top attraction names")
    recommended_hotels: list[str] = Field(default_factory=list, description="Hotel name suggestions")
    recommended_restaurants: list[str] = Field(default_factory=list, description="Restaurant name suggestions")


class TripPlanData(BaseModel):
    plan: TripPlan


class TripPlanResponse(BaseModel):
    success: bool = True
    data: TripPlanData
    message: str = "Trip plan generated successfully"
