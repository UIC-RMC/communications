#creator: Alex Domagala
#Module responsible for handling control input collection and sending/recieving data via protoBuffers
#Module uses TCP rather than UDP

#steps: make a new proto file that can package all the command data together
#make class that can actually send the protobuffer data

#https://stackoverflow.com/questions/40450556/how-to-know-which-protobuf-message-the-byte-array-is/50291651#50291651


import socket
import cmd_pb2 as pb

class protoSerializer:
    #for serializing all messsage types
    def __init__(self):
        self.movement = pb.movement()
        self.dumping = pb.dumping()
        self.mining = pb.mining()
        self.WrapperMessage = pb.WrapperMessage()

    def updateMovement(self, mtr_spd, mtr_ang):
        self.movement.mtr_spd = mtr_spd
        self.movement.mtr_ang = mtr_ang
        self.WrapperMessage.commonField = 1
        self.WrapperMessage.msg.m1 = self.movement

    def updateDumping(self, mtr_mining, extend, retract):
        self.dumping.mtr_mining = mtr_mining
        self.dumping.extend = extend
        self.dumping.retract = retract
        #elf.WrapperMessage.commonField = 2
        #self.WrapperMessage.m2 = self.dumping

    def updateMining(self, mtr_mining, extend, retract):
        self.mining.mtr_mining = mtr_mining
        self.mining.extend = extend
        self.mining.retract = retract
        #self.WrapperMessage.commonField = 3
        #self.WrapperMessage.m3 = self.mining

class protoDeserializer():
    #for deserializing all message types
    def __init__(self):
        self.movementMsg = pb.movement()
        self.dumpingMsg = pb.dumping()
        self.miningMsg = pb.mining()
        self.WrapperMessage = pb.WrapperMessage()

class transmitter:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SOCKET.bind((self.HOST, self.PORT))
        self.SOCKET.listen(1)
        self.CONN, self.ADDR = self.SOCKET.accept()
        print('Connected by: '+str(self.ADDR))

    def send_msg(self, message):
        self.CONN.sendall(message)

class reciever:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SOCKET.connect((self.HOST,self.PORT))
        self.RECIEVER = pb.WrapperMessage()

    #we actually need to wrap our messages
    def recieve_msg(self):
        #protobuffer is recieved over socket and still must be deserialized
        message = self.SOCKET.recv(1024)
        self.RECIEVER.ParseFromString(message)
        
        if self.RECIEVER.commonField == 1:
            print('Movement Message')
        if self.RECIEVER.commonField == 2:
            print('Dumping Message')
        if self.RECIEVER.commonField == 3:
            print('Mining Message')

