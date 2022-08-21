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
def getWeatherData():
    return ResponseHelper.getWeatherData()

@app.post("/weather/post")
def saveWeatherData(data: WeatherData):
    return ResponseHelper.writeWeatherData(data)

@app.delete("/weather/delete")
def deleteWeatherData():
    return ResponseHelper.deleteWeatherData()

@app.get("/events")
def getEvents():
    return ResponseHelper.getEvents()

@app.post("/events/post")
def saveEvent(event: Event):
    return ResponseHelper.saveEvent(event)

@app.delete("/events/delete")
def deleteEvent(event: Event):
    return ResponseHelper.deleteEvent(event)