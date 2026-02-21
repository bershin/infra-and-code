from fastapi import FastAPI

app=FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return{"user ID": user_id, "name": "John Berchin"}

# uvicorn 03get_user:app --reload
# http://127.0.0.1:8000/user/1