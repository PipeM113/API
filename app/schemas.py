from pydantic import BaseModel
from typing import Any

class PhotoCreate(BaseModel):
    image: Any 
    date: str
    location: dict

class PhotoResponse(BaseModel):
    id: str
    image_url: str
    date: str
    location: dict
    pothole_type: str
    confidence: float
