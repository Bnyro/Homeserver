from .models import *
from .config import *
import time
import json
import os

def joinDataDir():
    if not os.path.exists(dataDir):
        os.mkdir(dataDir)
    os.chdir(dataDir)

def getJSONFile(fileName: str):
    if not os.path.isfile(fileName):
            return []
    with open(fileName, 'r') as f:
        return json.load(f)

def writeJSON(fileName: str, data):
    with open(fileName, 'w') as outFile:
        json.dump(
            data,
            outFile,
            indent=4
        )

def getWeatherData() -> list:
    joinDataDir()
    return getJSONFile(weatherFile)

def writeWeatherData(weatherData: WeatherData) -> None:
    data = [{
        "time": time.time(),
        "data": weatherData.dict()
    }] + getWeatherData()
    joinWeatherDir()
    writeJSON(weatherFile, data)

def deleteWeatherData() -> None:
    joinWeatherDir()
    if os.path.isfile(weatherFile):
        os.remove(weatherFile)

def getEvents() -> list:
    joinDataDir()
    return getJSONFile(eventsFile)

def saveEvent(event: Event) -> None:
    joinDataDir()
    data = getEvents() + [event.dict()]
    writeJSON(eventsFile, data)

def deleteEvent(id: float) -> None:
    joinDataDir()
    data = [event for event in getEvents() if event["id"] != id]
    writeJSON(eventsFile, data)