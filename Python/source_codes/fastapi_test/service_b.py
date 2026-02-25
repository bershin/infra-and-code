from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# Define a GET endpoint that returns a simple message
@app.get("/endpoint")
def endpoint():
    return {"message": "Hello from Service B"}
