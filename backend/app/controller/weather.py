import requests
from typing import Any

from fastapi.encoders import jsonable_encoder

from app.model.response.weather import weatherResponse

class WeatherController:
    def __init__(self):
        self.key = "159d81ee8c094dc492132318240806"

    def build_forecast_body(self, body: dict[str, Any]):

        weather_dict = body.get("current")

        response_body = {
            "weather_condition": weather_dict["condition"]["text"],
            "weather_temperature": weather_dict["temp_c"],
            "weather_description": "weather description test",
            'weather_humidity': weather_dict["humidity"],
            "weather_wind_speed": weather_dict["wind_kph"]
        }

        return weatherResponse(**response_body)

    def get_forecast(self, city):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.key}&q={city}"

        response = self.build_forecast_body(requests.get(url).json())

        return response
