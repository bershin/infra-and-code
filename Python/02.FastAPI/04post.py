# Extracting JSON data using pydantic model.
# Make sure type value is correct.
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name:str
    price:float

@app.post("/item")
def create_item(item: Item):
    return{"message": f"Item {item.name} created with price {item.price}"}


# @app.post("/item", response_model=Item)
# def create_item(item: Item):
#     return item

# uvicorn 034post:app --reload
# http://127.0.0.1:8000/docs