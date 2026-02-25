from fastapi import FastAPI
import logging
import json
import socket

app = FastAPI()

# Configure logging
logger = logging.getLogger("fastapi_logstash_example")
logger.setLevel(logging.INFO)

# Logstash Handler Setup
class LogstashHandler(logging.Handler):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def emit(self, record):
        log_entry = self.format(record)
        self.sock.sendto(log_entry.encode("utf-8"), (self.host, self.port))

logstash_handler = LogstashHandler("logstash", 5000)
formatter = logging.Formatter(
    '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
)
logstash_handler.setFormatter(formatter)
logger.addHandler(logstash_handler)

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello, FastAPI with Logstash!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    logger.info(f"Item endpoint accessed with item_id: {item_id}")
    return {"item_id": item_id}
