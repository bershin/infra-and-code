# Customise the JSON response with status codes
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/items/")
async def create_item(name: str):
    return JSONResponse(status_code=201, content={"message": "Item created", "name": name})

# uvicorn 034post:app --reload
# http://127.0.0.1:8000/docs