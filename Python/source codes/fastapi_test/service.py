from fastapi import FastAPI

# Create a new FastAPI app instance
app = FastAPI()

# In-memory storage of items as a dictionary
items = {
    1: {"name": "Item 1", "description": "Description for Item 1"},
    2: {"name": "Item 2", "description": "Description for Item 2"},
}

# Define a GET endpoint to retrieve an item by its ID
@app.get("/items/{item_id}")
def read_item(item_id: int):
    # Try to get the item from the dictionary, or return an error message if not found
    return items.get(item_id, {"error": "Item not found"})
