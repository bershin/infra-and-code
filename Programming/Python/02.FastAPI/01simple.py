# Get a JSON message, Return Dictionary as JSON
# fastapi automatically transforms dictionary to JSON format
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"Message": "Hello world"}

# $ pip install fastapi[standard]
# Ask fastapi to start a server and give an url to access
# Fastapi uses uvicorn a lighting fast server to serve the app.
# $ fastapi dev main.py

# http://127.0.0.1:8000