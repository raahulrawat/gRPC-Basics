import grpc

# importing .proto generated packages
import df_pb2_grpc
import df_pb2

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = df_pb2_grpc.dataStub(channel)

# create a valid request message
number = df_pb2.Path(value="/home/rahul/Downloads/isChurn.csv")

# make the call
response = stub.read_data(number)

## getting response from the server and saving in data...
data = response.value

print(data)
