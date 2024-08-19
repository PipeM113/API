from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Configuración de la URI
uri = "mongodb+srv://felipe:<password>@geoviality.2zxqu4y.mongodb.net/?retryWrites=true&w=majority&appName=Geoviality"

# Crear un nuevo cliente y conectarse al servidor
client = MongoClient(uri, server_api=ServerApi('1'))

# Acceder a la base de datos
db = client['Geoviality'] 
