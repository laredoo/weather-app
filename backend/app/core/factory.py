from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.weather import weather

class WeatherAPI:
    def __init__(self):
        self.origins = [
            "http://localhost",
            "http://localhost:5500",
            "http://127.0.0.1",
            "http://127.0.0.1:5500",
        ]
        self.api = FastAPI()
        self.setup_middleware()
        self.setup_routes()

    def setup_middleware(self):
        self.api.add_middleware(
            CORSMiddleware,
            allow_origins=self.origins,  
            allow_credentials=True,
            allow_methods=["*"],  
            allow_headers=["*"],  
        )

    def setup_routes(self):
        self.api.include_router(weather.router)

    def create_api(self):
        return self.api
