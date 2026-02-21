from fastapi import FastAPI
from pydantic import BaseModel 

app=FastAPI()
class Supplier(BaseModel):
    name: str
    location: str
class Item(BaseModel):
    id: int
    price: float
    supplier: Supplier
@app.post("/items/")
def submit_item(item: Item):
    supplier={"name":"Geo", "Item":"Phone"}
    return{"Item": item.id, "price": item.price, "supplier": supplier}

