from pydantic import BaseModel, Field


class Hotel(BaseModel):
    id: str = Field(..., description="Unique hotel identifier")
    name: str = Field(..., description="Hotel name")
    description: str = Field(default="", description="Short description")
    address: str = Field(default="", description="Street address")
    latitude: float = Field(..., ge=-90.0, le=90.0, description="Latitude coordinate")
    longitude: float = Field(..., ge=-180.0, le=180.0, description="Longitude coordinate")
    image_url: str = Field(default="", description="Preview image URL")
    rating: float = Field(default=0.0, ge=0.0, le=5.0, description="Quality rating 0-5")
    price_level: str = Field(default="mid_range", description="Price tier: budget, mid_range, luxury")
    star_rating: int = Field(default=0, ge=0, le=5, description="Star rating 0-5")


class HotelsData(BaseModel):
    hotels: list[Hotel] = Field(default_factory=list)


class HotelsResponse(BaseModel):
    success: bool = True
    data: HotelsData
    message: str = "Hotels retrieved successfully"
