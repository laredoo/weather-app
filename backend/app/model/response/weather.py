from pydantic import BaseModel

class weatherResponse(BaseModel):
    weather_condition: str
    weather_temperature: float
    weather_description: str
    weather_humidity: int
    weather_wind_speed: float
    weather_icon: str
