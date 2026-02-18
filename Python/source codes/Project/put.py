from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()
class Item(BaseModel):
    name:str
    price:float
    
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} has been deleted"}


