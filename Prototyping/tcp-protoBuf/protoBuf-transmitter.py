#https://www.youtube.com/watch?v=Lbfe3-v7yE0
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