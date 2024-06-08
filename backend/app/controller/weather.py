from fastapi.encoders import jsonable_encoder
import requests

class WeatherController:
    def __init__(self):
        self.key = "159d81ee8c094dc492132318240806"

    def get_forecast(self, city):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.key}&q={city}"

        response = requests.get(url)

        return response.json()
