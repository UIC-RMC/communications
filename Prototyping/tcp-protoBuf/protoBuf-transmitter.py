
'''#https://www.youtube.com/watch?v=Lbfe3-v7yE0
import socket
import time

HOST = socket.gethostname()
PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5) #listen for communications

while True:
    clientsocket, address = s.accept()
    print(f'connection from {address}')
    clientsocket.send(bytes('Hello World!','utf-8'))
    time.sleep(2)
    print('active')
'''

# echo-server.py

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)