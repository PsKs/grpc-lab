# -*- coding: utf-8 -*-
import time
import grpc
import greeter_pb2
import greeter_pb2_grpc

def get_client_stream_request():
    while True:
        name = input("Enter a name (or nothing to stop chatting): ")
        
        if not name:
            break
        
        yield greeter_pb2.HelloRequest(name=name, greeting="Konnichiwa")
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary RPC")
        print("2. ParrotSaysHello - Server Streaming RPC")
        print("3. ChattyClientSaysHello - Client Streaming RPC")
        print("4. InteractingHello - Bidirectional Streaming RPC")
        rpc_call = input("Enter the RPC call number: ")
        
        if rpc_call == "1":
            hello_request = greeter_pb2.HelloRequest(name="John", greeting="Hello")
            hello_reply = stub.SayHello(hello_request)
            print("Greeter client received: " + hello_reply.message)

        elif rpc_call == "2":
            hello_request = greeter_pb2.HelloRequest(name="John", greeting="Bounjour")
            hello_replies = stub.ParrotSaysHello(hello_request)
            
            for hello_reply in hello_replies:
                print("Greeter client received: " + hello_reply.message)

        elif rpc_call == "3":
            delayed_reply = stub.ChattyClientSaysHello(get_client_stream_request())
            print("ChattyClientSaysHello client received: ")
            print(delayed_reply)

        elif rpc_call == "4":
            responses = stub.InteractingHello(get_client_stream_request())
            
            for response in responses:
                print("InteractingHello received: ")
                print(response)
            
if __name__ == '__main__':
    run()