from pydantic import BaseModel, Field

from app.schemas.common import PaginationMeta


class GeocodingResult(BaseModel):
    id: str = Field(..., description="Unique place identifier")
    name: str = Field(..., description="Place name")
    display_name: str = Field(..., description="Full display address")
    latitude: float = Field(..., ge=-90.0, le=90.0, description="Latitude coordinate")
    longitude: float = Field(..., ge=-180.0, le=180.0, description="Longitude coordinate")
    country: str = Field(default="", description="Country name")
    country_code: str = Field(default="", description="ISO 3166-1 alpha-2 country code")
    region: str = Field(default="", description="State or region")
    city: str = Field(default="", description="City or town name")
    place_type: str = Field(default="", description="Nominatim place type")
    importance: float = Field(default=0.0, description="Nominatim importance score")


class GeocodingData(BaseModel):
    results: list[GeocodingResult] = Field(default_factory=list)
    query: str = Field(..., description="Original search query")
    pagination: PaginationMeta


class GeocodingResponse(BaseModel):
    success: bool = True
    data: GeocodingData
    message: str = "Locations retrieved successfully"
