from models import WeatherData, Event
from config import *
import message
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

def writeWeatherData(weatherData: WeatherData) -> dict:
    data = [{
        "time": time.time(),
        "data": weatherData.dict()
    }] + getWeatherData()
    joinWeatherDir()
    writeJSON(weatherFile, data)
    return message.ok

def deleteWeatherData() -> dict:
    joinWeatherDir()
    if os.path.isfile(weatherFile):
        os.remove(weatherFile)
    return message.ok

def getEvents() -> list:
    joinDataDir()
    return getJSONFile(eventsFile)

def saveEvent(event: Event) -> dict:
    joinDataDir()
    data = getEvents() + [event.dict()]
    writeJSON(eventsFile, data)
    return message.ok

def deleteEvent(id: float) -> dict:
    joinDataDir()
    data = [event for event in getEvents() if event["id"] != id]
    writeJSON(eventsFile, data)
    return message.ok