from pydantic import BaseModel, Field

from app.schemas.common import PaginationMeta


class Destination(BaseModel):
    id: str = Field(..., description="Unique destination identifier slug")
    name: str = Field(..., description="Destination name")
    country: str = Field(default="", description="Country name")
    region: str = Field(default="", description="Region or state")
    slug: str = Field(default="", description="URL-friendly slug")
    latitude: float = Field(..., ge=-90.0, le=90.0, description="Latitude coordinate")
    longitude: float = Field(..., ge=-180.0, le=180.0, description="Longitude coordinate")
    description: str = Field(default="", description="Short destination description")
    image_url: str = Field(default="", description="Primary image URL")
    highlights: list[str] = Field(default_factory=list, description="Key highlights or themes")
    best_time_to_visit: str = Field(default="", description="Best season or months to visit")
    travel_type: str = Field(default="", description="Category: City, Beach, Nature, etc.")


class DestinationSearchData(BaseModel):
    results: list[Destination] = Field(default_factory=list)
    query: str = Field(..., description="Original search query")
    pagination: PaginationMeta


class DestinationDetailData(BaseModel):
    destination: Destination


class FeaturedDestinationsData(BaseModel):
    destinations: list[Destination] = Field(default_factory=list)


class DestinationSearchResponse(BaseModel):
    success: bool = True
    data: DestinationSearchData
    message: str = "Destinations retrieved successfully"


class DestinationDetailResponse(BaseModel):
    success: bool = True
    data: DestinationDetailData
    message: str = "Destination details retrieved successfully"


class FeaturedDestinationsResponse(BaseModel):
    success: bool = True
    data: FeaturedDestinationsData
    message: str = "Featured destinations retrieved successfully"
