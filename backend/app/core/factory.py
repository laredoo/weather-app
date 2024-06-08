from fastapi import FastAPI

from app.api.weather import weather



def create_api():
    """
        Function used for creating our API
    """
    api = FastAPI()

    api.include_router(weather.router)

    return api