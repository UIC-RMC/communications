import serdes
import tcpModule

HOST = '192.168.1.162'
PORT = 61626

#create serializer and reciever objects
ser = serdes.deserializer()
recv = tcpModule.reciever(HOST, PORT)

#recieve messages
while True:
    msg = recv.recieve_msg()
    ser.decode(msg)
