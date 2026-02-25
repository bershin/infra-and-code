from multiprocessing import Process
from fastapi.testclient import TestClient
import time
import requests
from service_a import app as app_a  # Import Microservice A
from service_b import app as app_b  # Import Microservice B

# Assuming app_a is the FastAPI app for Microservice A
# and app_b is the FastAPI app for Microservice B

def run_service_b():
    import uvicorn
    uvicorn.run("service_b:app", host="127.0.0.1", port=8001)

def test_call_service_b():
    process_b = Process(target=run_service_b)
    process_b.start()

    # Wait for Microservice B to start
    time.sleep(5)  # Increased wait time

    # TestClient for Microservice A
    client_a = TestClient(app_a)

    try:
        # Simulate a GET request to /call-service-b in Microservice A
        response = client_a.get("/call-service-b")
        assert response.status_code == 200  # Or whatever status you expect
        assert response.json() == {"result": {"message": "Hello from Service B"}}
        

    finally:
        # Ensure the process is terminated
        process_b.terminate()
        process_b.join()

# Optional: Run the test directly if this script is executed
if __name__ == "__main__":
    test_call_service_b()
