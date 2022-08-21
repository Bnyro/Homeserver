from pydantic import BaseModel

class WeatherData(BaseModel):
    ds18_t: float
    dht_t: float
    dht_h: float
    bmp_t: float
    bmp_p: float

class Event(BaseModel):
    title: str
    start: str