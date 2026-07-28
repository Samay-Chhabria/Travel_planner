from pydantic import BaseModel, Field


class CurrentWeather(BaseModel):
    temperature_c: float = Field(..., description="Current temperature in Celsius")
    temperature_f: float = Field(..., description="Current temperature in Fahrenheit")
    condition: str = Field(..., description="Short weather condition label")
    description: str = Field(..., description="Human-readable weather description")


class ForecastDay(BaseModel):
    date: str = Field(..., description="Forecast date in YYYY-MM-DD format")
    max_temp_c: float = Field(..., description="Maximum temperature in Celsius")
    min_temp_c: float = Field(..., description="Minimum temperature in Celsius")
    condition: str = Field(..., description="Short weather condition label")


class WeatherData(BaseModel):
    destination_id: str = Field(..., description="Destination identifier slug")
    current: CurrentWeather
    forecast: list[ForecastDay] = Field(default_factory=list)


class WeatherSuccessData(BaseModel):
    weather: WeatherData


class WeatherResponse(BaseModel):
    success: bool = True
    data: WeatherSuccessData
    message: str = "Weather data retrieved successfully"
