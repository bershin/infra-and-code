import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/order/{product_id}")
def create_order(product_id: int):
    product_response = requests.get(f"http://product-service/products/{product_id}")
    product = product_response.json().get("product")
    if product:
        return {"order": f"Order created for {product['name']} at {product['price']}$"}
    return {"error": "Product not found"}
