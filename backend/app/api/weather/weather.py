from fastapi import APIRouter, HTTPException

from app.model.request.weather import Weather as Weather_Model
from app.model.response.weather import weatherResponse

from app.controller.weather import WeatherController

weather_controller = WeatherController()

router = APIRouter()

class Weather: 

    @router.get("/weather")
    def check_weather(
        city: str = None
    ) -> weatherResponse:
        if not input:
            raise HTTPException(status_code=500, detail="No input given")
        
        response_dict = weather_controller.get_forecast(city)
        return response_dict