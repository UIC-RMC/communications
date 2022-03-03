import socket
import test_pb2 as pb2

host = "192.168.1.162"
port = 61626
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.sendall(b'Hello, world')
while True:
    data = s.recv(1024)
    print(repr(data))
s.close()