import uuid
from database import db
from bson import ObjectId

def save_image(image):
    # Generar un nombre único usando UUID
    image_uuid = str(uuid.uuid4())
    image_extension = ".png"
    image_filename = f"{image_uuid}{image_extension}"
    
    # Ubicación donde se guardará la imagen
    file_location = f"services/imgs/{image_filename}"
    
    # Guardar la imagen en la carpeta /services/imgs
    with open(file_location, "wb") as f:
        f.write(image.file.read())
    
    return file_location, image_filename

def save_data_to_mongodb(image_filename, latitude, longitude, date):
    collection = db['images']
    
    data = {
        "image_filename": image_filename,
        "latitude": latitude,
        "longitude": longitude,
        "date": date,
        "_id": str(ObjectId())
    }
    
    result = collection.insert_one(data)
    return result.inserted_id



