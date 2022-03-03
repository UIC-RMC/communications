
#https://www.youtube.com/watch?v=Lbfe3-v7yE0
#https://notenoughtech.com/raspberry-pi/rpi-socket-protocol/
'''
import socket

HOST = '' # Server IP or Hostname
PORT = 12345 # Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#managing error exception
try:
	s.bind((HOST, PORT))
	s.listen(5)
	print('Socket awaiting messages')
	(conn, addr) = s.accept()
	print('Connected')
except:
        print('fail bind')

# awaiting for message
while True:
	data = conn.recv(1024)
	print('I sent a message back in response to: ' + data)
	reply = ''
	conn.close() # Close connections
	'''

import socket

host = ''
port = 61626

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print(host, port)

s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    try:
        data = conn.recv(1024)

        if not data: break

        print("Client says:")
        print(data)
        conn.sendall(b"Server says: hi")

    except socket.error:
        print("Error Occured")
        break

conn.close()