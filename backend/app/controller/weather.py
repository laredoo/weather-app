import requests
from typing import Any

from fastapi.encoders import jsonable_encoder
from app.model.response.weather import weatherResponse

class WeatherController:
    def __init__(self):
        self.api_key = "159d81ee8c094dc492132318240806"
        self.base_url = "http://api.weatherapi.com/v1/current.json"

    def build_forecast_body(self, body: dict[str, Any]) -> weatherResponse:
        weather_dict = body.get("current")
        if not weather_dict:
            raise ValueError("Invalid response from weather API")

        response_body = {
            "weather_condition": weather_dict["condition"]["text"],
            "weather_temperature": weather_dict["temp_c"],
            "weather_description": weather_dict["condition"]["text"],
            "weather_humidity": weather_dict["humidity"],
            "weather_wind_speed": weather_dict["wind_kph"],
            "weather_icon": weather_dict["condition"]["icon"],
        }

        return weatherResponse(**response_body)

    def get_forecast(self, city: str) -> weatherResponse:
        if not city:
            raise ValueError("City name cannot be empty")

        url = f"{self.base_url}?key={self.api_key}&q={city}"

        response = requests.get(url)
        if response.status_code != 200:
            raise requests.HTTPError(f"Error fetching weather data: {response.status_code}")

        response_data = response.json()
        return self.build_forecast_body(response_data)
