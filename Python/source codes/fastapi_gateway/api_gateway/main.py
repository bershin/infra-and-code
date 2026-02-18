# Import required libraries
from fastapi import FastAPI, Request, Depends, HTTPException
import httpx

# Create an instance of FastAPI
app = FastAPI()

# Function to simulate token validation
async def validate_token(token: str):
    if token != "valid-token":
        raise HTTPException(status_code=403, detail="Unauthorized")

# API Gateway endpoint to route requests
@app.get("/api/service-a")
async def proxy_service_a(request: Request, token: str = Depends(validate_token)):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://service-a:8000/service-a")
    return response.json()

# API Gateway endpoint to route requests
@app.get("/api/service-b")
async def proxy_service_b(request: Request, token: str = Depends(validate_token)):
    async with httpx.AsyncClient() as client:
        response = await client.get("http://service-b:8000/service-b")
    return response.json()
