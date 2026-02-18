from fastapi import FastAPI

app=FastAPI()
@app.post("/items/{item}")
def create_supplier_item(item: str):
    supplier={"name":"Geo", "Item":"Phone"}
    return{"Item": item, "supplier": supplier}

