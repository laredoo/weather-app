from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.weather import weather

origins = [
    "http://localhost",
    "http://localhost:5500",
    "http://127.0.0.1",
    "http://127.0.0.1:5500",
]

def create_api():
    """
        Function used for creating our API
    """
    api = FastAPI()

    api.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  
        allow_credentials=True,
        allow_methods=["*"],  
        allow_headers=["*"],  
    )

    api.include_router(weather.router)

    return api