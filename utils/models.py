from pydantic import BaseModel

class WeatherData(BaseModel):
    ds18_t: float
    dht_t: float
    dht_h: float
    bmp_t: float
    bmp_p: float

class WeatherItem(BaseModel):
    time: float
    data: WeatherData

class Event(BaseModel):
    id: float
    title: str | None = None
    start: str | None = None
    end: str | None = None
    color: str | None = None

class Message(BaseModel):
    message: str