import socket
import test_pb2 as pb2

#data recieving object
pbRecieve = pb.data()

host = "192.168.1.162"
port = 61626
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


while True:
    data = s.recv(1024)
    #update the receiving object and set a length
    length = pbRecieve.ParseFromString(data)
    #print(repr(data))

    print(pbRecieve.id)
    print(pbRecieve.name)
    print(pbRecieve.decimal)

s.close()