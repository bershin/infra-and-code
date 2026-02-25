# Import required libraries
from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define a simple GET endpoint
@app.get("/service-b")
async def read_service_b():
    return {"message": "Response from Service B"}
