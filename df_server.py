import grpc
from concurrent import futures
import time

"""
import here proto generated packages 

command : python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. df.proto

:param : dataServicer and add_dataServicer_to_server will be generated 
"""
import df_pb2
import df_pb2_grpc

# import the main function file here, for this case it is DF.py
import DF

# create a class here to consume the generated class by proto.
# dataServicer(for this case)
class df_server(df_pb2_grpc.dataServicer):

    ## loading a read_data function here from the generated packages and take a input here from the client and use the main function to load the data..
    def read_data(self, request, context):
        response = df_pb2.Path()
        print(request.value)
        response.value = DF.read_file(request.value)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_dataServicer_to_server`
# to add the defined class to the server
df_pb2_grpc.add_dataServicer_to_server(df_server(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)