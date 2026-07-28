from pydantic import BaseModel, Field


class Attraction(BaseModel):
    id: str = Field(..., description="Unique attraction identifier")
    name: str = Field(..., description="Attraction name")
    category: str = Field(default="", description="Category: museum, monument, natural, etc.")
    description: str = Field(default="", description="Short description of the attraction")
    address: str = Field(default="", description="Street address")
    latitude: float = Field(..., ge=-90.0, le=90.0, description="Latitude coordinate")
    longitude: float = Field(..., ge=-180.0, le=180.0, description="Longitude coordinate")
    image_url: str = Field(default="", description="Preview image URL")
    rating: float = Field(default=0.0, ge=0.0, le=5.0, description="Quality rating 0-5")


class AttractionsData(BaseModel):
    attractions: list[Attraction] = Field(default_factory=list)


class AttractionsResponse(BaseModel):
    success: bool = True
    data: AttractionsData
    message: str = "Attractions retrieved successfully"
