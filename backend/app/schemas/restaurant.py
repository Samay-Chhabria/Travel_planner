from pydantic import BaseModel, Field


class Restaurant(BaseModel):
    id: str = Field(..., description="Unique restaurant identifier")
    name: str = Field(..., description="Restaurant name")
    description: str = Field(default="", description="Short description")
    address: str = Field(default="", description="Street address")
    latitude: float = Field(..., ge=-90.0, le=90.0, description="Latitude coordinate")
    longitude: float = Field(..., ge=-180.0, le=180.0, description="Longitude coordinate")
    image_url: str = Field(default="", description="Preview image URL")
    rating: float = Field(default=0.0, ge=0.0, le=5.0, description="Quality rating 0-5")
    cuisine_type: str = Field(default="", description="Primary cuisine type")
    price_level: str = Field(default="mid_range", description="Price tier: budget, mid_range, luxury")


class RestaurantsData(BaseModel):
    restaurants: list[Restaurant] = Field(default_factory=list)


class RestaurantsResponse(BaseModel):
    success: bool = True
    data: RestaurantsData
    message: str = "Restaurants retrieved successfully"
