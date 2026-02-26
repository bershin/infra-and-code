from fastapi import FastAPI

app=FastAPI()
@app.post("/items/{item}")
def create_supplier_item(item: int):
    supplier={"name":"Geo", "Item":"Phone"}
    return{"Item": item, "price": 20.5, "supplier": supplier}

