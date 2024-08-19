from fastapi import APIRouter, File, UploadFile, Form
from controllers import save_image, save_data_to_mongodb
from schemas import LocationSchema
from datetime import date

router = APIRouter()

@router.post("/upload")
async def upload_data(
    image: UploadFile = File(...),
    latitude: float = Form(...),
    longitude: float = Form(...),
    date: date = Form(...)
):
    
    _, image_filename = save_image(image)
    
    save_data_to_mongodb(image_filename, latitude, longitude, date)
    
    return {"message": "Data uploaded successfully"}
