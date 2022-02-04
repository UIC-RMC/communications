#creator: Alex Domagala
#Main Program that is run on the raspberryPi, responsible for recieiving control commands from control computer

from udpModule import reciever
from commandModule import movementControl
import threading
import time

#Connection Parameters
UDP_Port = 5005                                     #specifies unused port on network
LOCAL_IP = '0.0.0.0'                                #specifies IPv4 addresses on the local machine (raspberryPi)
UDP_IP = '192.168.1.162'                            #target IP address (external Computer)

#Instatiate modules and run necessary threads
recieve = reciever(UDP_Port, LOCAL_IP, UDP_IP)      #instantiate reciever object
move = movementControl()                            #instantiate movement object
t = threading.Thread(target=recieve.recv_msg)       #thread will handle recieving of messages
t.start()
t2 = threading.Thread(target=recieve.send_msg)      #thread will handle sending of messages
t2.start()

#Event handler for running robot
while True:

    a = (recieve.msg.split(' '))                    #Recieve a message from reciever, split message into x, y components
    try:
        x = int(float(a[0]) * 1000)                 #Convert message to integer for Roboteq (xAxis)
        y = -1 * int(float(a[1]) * 1000)            #Convert message to integer for Roboteq (yAxis)
        move.control(x,y)
    except:
       pass
    time.sleep(.25)