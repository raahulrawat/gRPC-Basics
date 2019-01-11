# gRPC-Basics
To get started with gRPC installing it:
                                        python -m pip install grpcio
In gRPC, there are three main parts are proto file, server and client.
In this example proto file is df.proto, server file is df_server.py and client file is df_client.py
compile the proto file and get two generate packages like df_pb2_grpc.py, df_pb2.py. These packages will be used in server and client as well to communicate with the server.
To compile proto file command is : python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. df.proto
client can be written in different languange. For this example python client has been created for testing purpose.
