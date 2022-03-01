import socket

HOST = '192.168.0.102'
PORT = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

s.listen(1)
(conn, addr) = s.accept()

while True:
    data = conn.recv(1024)
    print(data)