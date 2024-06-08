from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_temperature():
    return {"temperature": "20 graus"}


