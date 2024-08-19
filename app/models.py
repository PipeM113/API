from pydantic import BaseModel
from datetime import date

class LocationData(BaseModel):
    latitude: float
    longitude: float
    date: date
