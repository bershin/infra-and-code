from fastapi.responses import JSONResponse
from fastapi import FastAPI

app = FastAPI()

@app.post("/items/")
async def create_item(name: str):
    return JSONResponse(status_code=201, content={"message": "Item created", "name": name})
