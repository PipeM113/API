from fastapi import FastAPI
from dotenv import load_dotenv
from routes import router as api_router
import os

load_dotenv()

app = FastAPI()

app.include_router(api_router)

host = os.getenv("HOST")
port = int(os.getenv("PORT_NUMBER"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=host, port=port)