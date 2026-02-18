# Import required libraries
from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define a simple GET endpoint
@app.get("/service-a")
async def read_service_a():
    return {"message": "Response from Service A"}
