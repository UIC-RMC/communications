import serdes
import tcpModule
from time import sleep

HOST = ''
PORT = 61626

#create serializer and transmitter objects
ser = serdes.serializer()
trans = tcpModule.transmitter(HOST, PORT)

#example: we want to send a movement message
ser.updateMovement(555,352)
msg = ser.serialize() #msg is the serialized movement command

#send the message every 2 seconds
while True:
    trans.send_msg(msg)
    sleep(2)