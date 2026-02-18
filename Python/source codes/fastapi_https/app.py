from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# Define a root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, Secure World!"}

if __name__ == "__main__":
    import uvicorn
    # Running the Uvicorn server with HTTPS
    uvicorn.run("app:app", host="0.0.0.0", port=8000, ssl_keyfile="key.pem", ssl_certfile="cert.pem")
