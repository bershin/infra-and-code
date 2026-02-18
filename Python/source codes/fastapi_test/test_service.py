from fastapi.testclient import TestClient  # Import TestClient for testing
from service import app  # Import the FastAPI app instance from service.py

# Create a TestClient instance to simulate requests to the API
client = TestClient(app)

# Test case to check if an existing item can be retrieved
def test_read_item():
    # Simulate a GET request to the endpoint with item_id = 1
    response = client.get("/items/1")
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Assert that the JSON response matches the expected item data
    assert response.json() == {"name": "Item 1", "description": "Description for Item 1"}

# Test case to check the behavior when requesting a nonexistent item
def test_read_nonexistent_item():
    # Simulate a GET request for a nonexistent item (e.g., item_id = 999)
    response = client.get("/items/999")
    
    # Assert that the response status code is 200 (OK), even though the item wasn't found
    assert response.status_code == 200
    
    # Assert that the response contains an error message
    assert response.json() == {"error": "Item not found"}
