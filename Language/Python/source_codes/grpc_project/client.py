import grpc
import service_pb2_grpc as pb2_grpc
import service_pb2 as pb2
from fastapi import FastAPI

app = FastAPI()

def grpc_client(message):
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.DataTransferStub(channel)
    request = pb2.DataRequest(message=message)
    response = stub.SendData(request)
    return response.status

@app.post("/send-data/")
def send_data(message: str):
    status = grpc_client(message)
    return {"status": status}
