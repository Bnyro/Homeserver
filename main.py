from fastapi import FastAPI
from models.weatherData import WeatherData
import dependencies.ResponseHelper as ResponseHelper
import os
import json

app = FastAPI()

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
