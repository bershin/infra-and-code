from fastapi import FastAPI
from pydantic import BaseModel 

app=FastAPI()
class Supplier(BaseModel):
    name: str
    location: str
class Item(BaseModel):
    name: str
    price: str
    supplier: Supplier
@app.post("/items/{item_id}")
def create_supplier_item(item_id: str, item: Item):
    return {
        "item_id": item_id,
        "item": item
    }

