from fastapi import APIRouter, HTTPException
from app.model.request.weather import Weather as Weather_Model
from app.model.response.weather import weatherResponse
from app.controller.weather import WeatherController

router = APIRouter()

class WeatherAPI:
    def __init__(self):
        self.weather_controller = WeatherController()

    def setup_routes(self):
        router.add_api_route("/weather", self.check_weather, methods=["GET"])

    def check_weather(self, city: str = None) -> weatherResponse:
        if not city:
            raise HTTPException(status_code=500, detail="No input given")
        
        response_dict = self.weather_controller.get_forecast(city)
        return response_dict

weather_api = WeatherAPI()
weather_api.setup_routes()
