# -*- coding: utf-8 -*-
from concurrent import futures
import time

import grpc
import greeter_pb2
import greeter_pb2_grpc

class GreeterServicer(greeter_pb2_grpc.GreeterServicer):
    # Simple RPC
    def SayHello(self, request, context):
        print("Received request from client: ")
        print(request)
        
        return greeter_pb2.HelloReply(message='%s, %s!' % (request.greeting, request.name))
    
    # Response-streaming RPC (Server Streaming)
    def ParrotSaysHello(self, request, context):
        print("ParrotSaysHello received request from client: ")
        print(request)
        
        for i in range(3):
            yield greeter_pb2.HelloReply(message='Line %i: %s, %s!' % (i + 1, request.greeting, request.name))
            time.sleep(2)
    
    # Request-streaming RPC (Client Streaming)
    def ChattyClientSaysHello(self, request_iterator, context):
        delayed_reply = greeter_pb2.DelayedReply()
        
        for request in request_iterator:
            print("ChattyClientSaysHello received request from client: ")
            print(request)
            delayed_reply.request.append(request)
            
        delayed_reply.message = "You sent %i requests. Please expect a delayed response." % len(delayed_reply.request)
        
        return delayed_reply
    
    # Bidirectional streaming RPC
    def InteractingHello(self, request_iterator, context):
        for request in request_iterator:
            print("InteractingHello received request from client: ")
            print(request)
            
            yield greeter_pb2.HelloReply(message='Received request: %s, %s!' % (request.greeting, request.name))
            time.sleep(2)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()