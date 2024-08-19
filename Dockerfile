FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]

# Crear imagen:
# docker build -t geoviality-api-image .

# Correr contenedor:
# docker run -d --name geoviality-api-container -p 8000:8000 -v ".:/app" geoviality-api-image