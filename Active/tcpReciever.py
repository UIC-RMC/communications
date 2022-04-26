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
    data = ser.decode(msg) #note that data is a python list that contains the different values
    print(data[0]) #contains the message type

    #do the stuff based on the data
    if data[0] == 'move':
        pass

    elif data[0] == 'mine':
        pass

    elif data[0] == 'dump':
        pass
