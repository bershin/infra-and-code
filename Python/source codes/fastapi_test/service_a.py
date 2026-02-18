from fastapi import FastAPI
import requests  # To send HTTP requests to other services

# Create FastAPI app instance
app = FastAPI()

# Define a GET endpoint that calls Microservice B
@app.get("/call-service-b")
def call_service_b():
    # Make an HTTP GET request to Microservice B at localhost:8001/endpoint
    response = requests.get("http://localhost:8001/endpoint")
    
    # Return the JSON response received from Microservice B
    return {"result": response.json()}
