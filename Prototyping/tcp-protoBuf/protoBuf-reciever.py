import socket

HOST = socket.gethostname()
PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

msg = s.recv(1024)
print(msg.decode('utf-8'))