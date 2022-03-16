#basic protobuffer example - complete

import socket
import time
import test_pb2 as pb

#the data we are going to send
#first we create pbSend which is from the python protobuffer class
#then we update the parameters we actually want to send
pbSend = pb.data()
pbSend.id = 123455
pbSend.name = "test"
pbSend.decimal = 2.34
#finally we create "testData", this is in binary from serializing
testData = pbSend.SerializeToString()

host = ''
port = 61626

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

while True:
	#for recieving
	#data = conn.recv(1024)
	#print("Client says:" + data)

	#send the testing data bytes
	conn.sendall(testData)
	time.sleep(2)

conn.close()