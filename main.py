from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import WeatherData, Event
import ResponseHelper as ResponseHelper
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

@app.get("/weather/data")
def get_weather_data():
    return ResponseHelper.getWeatherData()

@app.post("/weather/post")
def save_weather_data(data: WeatherData):
    return ResponseHelper.writeWeatherData(data)

@app.delete("/weather/delete")
def delete_weather_data():
    return ResponseHelper.deleteWeatherData()

@app.get("/events")
def get_events():
    return ResponseHelper.getEvents()

@app.post("/events/post")
def save_event(event: Event):
    return ResponseHelper.saveEvent(event)

@app.delete("/events/delete")
def delete_event(event: Event):
    return ResponseHelper.deleteEvent(event.id)