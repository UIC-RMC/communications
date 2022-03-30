import socket

class transmitter:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SOCKET.bind((self.HOST, self.PORT))
        self.SOCKET.listen(1)
        self.CONN, self.ADDR = self.SOCKET.accept()
        print('Connected by: '+str(self.ADDR))

    #msg sent must be a serial form (must still be serialized)
    def send_msg(self, msg):
        self.CONN.sendall(msg)

class reciever:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SOCKET.connect((self.HOST,self.PORT))

    #msg recieved will be a serial form (must still be deserialized)
    def recieve_msg(self):
        msg = self.SOCKET.recv(1024)
        return msg
