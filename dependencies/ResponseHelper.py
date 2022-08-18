from models.weatherData import WeatherData
from .config import *
import time
import json
import os

def joinWeatherDir():
    os.chdir(homeDir)
    if not os.path.exists(folderName):
        os.mkdir(folderName)
    os.chdir(os.path.join(homeDir, folderName))

def getWeatherData() -> list:
    joinWeatherDir()
    if not os.path.isfile(fileName):
        return []
    with open(fileName, 'r') as f:
        return json.load(f)

def writeWeatherData(weatherData: WeatherData) -> dict:
    data = [{
        "time": time.time(),
        "data": weatherData.dict()
    }] + getWeatherData()
    joinWeatherDir()
    with open(fileName, 'w') as f:
        json.dump(data, f, indent=4)
    return {"message": "ok"}

def deleteWeatherData() -> dict:
    joinWeatherDir()
    if os.path.isfile(fileName):
        os.remove(fileName)
    return {"message", "ok"}