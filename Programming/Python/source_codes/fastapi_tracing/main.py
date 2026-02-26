from fastapi import FastAPI
import opentracing
from jaeger_client import Config

app = FastAPI()

# Initialize Jaeger tracer
def init_tracer(service_name='fastapi-jaeger'):
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'logging': True,
        },
        service_name=service_name,
    )
    return config.initialize_tracer()

tracer = init_tracer()

@app.get("/")
def read_root():
    with tracer.start_active_span('root-endpoint'):
        return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    with tracer.start_active_span('item-endpoint'):
        return {"item_id": item_id}
