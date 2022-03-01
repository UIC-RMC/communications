import socket

HOST = '192.168.0.120'
PORT = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    txt = input('enter msg: ')
    s.send(txt)