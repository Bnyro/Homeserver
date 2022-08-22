from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.models import *
import utils.ResponseHelper as ResponseHelper
import os
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API online"}

@app.get("/weather/data", response_model=list[WeatherItem])
def get_weather_data():
    return ResponseHelper.getWeatherData()

@app.post("/weather/post", response_model=Message)
def save_weather_data(data: WeatherData):
    ResponseHelper.writeWeatherData(data)
    return Message(message="ok")

@app.delete("/weather/delete", response_model=Message)
def delete_weather_data():
    ResponseHelper.deleteWeatherData()
    return Message(message="ok")

@app.get("/events", response_model=list[Event])
def get_events():
    return ResponseHelper.getEvents()

@app.post("/events/post", response_model=Message)
def save_event(event: Event):
    ResponseHelper.saveEvent(event)
    return Message(message="ok")

@app.delete("/events/delete", response_model=Message)
def delete_event(event: Event):
    ResponseHelper.deleteEvent(event.id)
    return Message(message="ok")