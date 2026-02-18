from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Supplier(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str
    price: float
    supplier: Supplier

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    supplier = {"name": "Supplier Name", "location": "City"}
    return {"name": "Item Name", "price": 20.5, "supplier": supplier}
