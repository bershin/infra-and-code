from fastapi import FastAPI
import redis

#Connect to Redis service(find the hostname from docker compose)
r = redis.Redis(host='redis', port=6379)

app=FastAPI()

@app.get("/")
def read_root():
    count=r.incr("hits")
    return{"message": "Hello, FastAPI with Redis!", "visit_count": count}