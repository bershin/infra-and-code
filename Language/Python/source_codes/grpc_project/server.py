import grpc
from concurrent import futures
import service_pb2_grpc as pb2_grpc
import service_pb2 as pb2
from fastapi import FastAPI

class DataTransferService(pb2_grpc.DataTransferServicer):
    def SendData(self, request, context):
        message = request.message
        print(f"Received message: {message}")
        return pb2.DataResponse(status="Success")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_DataTransferServicer_to_server(DataTransferService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

app = FastAPI()

@app.on_event("startup")
def startup_event():
    import threading
    server_thread = threading.Thread(target=serve)
    server_thread.start()
