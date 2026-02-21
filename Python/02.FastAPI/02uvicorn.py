# Run the app directly
# Return Dictionary as JSON
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"Message": "Hello unicorn"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8200)

# python 02uvicorn.py
# http://127.0.0.1:8000