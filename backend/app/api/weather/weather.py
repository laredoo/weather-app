from fastapi import APIRouter, HTTPException

from app.model.weather import Weather as Weather_Model

from app.controller.weather import WeatherController

weather_controller = WeatherController()

router = APIRouter()

class Weather: 

    @router.post("/")
    def check_weather(
        input: Weather_Model = None
    ):
        if not input:
            print("im here")
            raise HTTPException(status_code=500, detail="No input given")
        
        response_dict = weather_controller.get_forecast(input.city_name)    
        return response_dict