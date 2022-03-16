#creator: Alex Domagala
#Main Program that is run on the control computer, responsible for sending control commands to the raspberryPi

from udpModule import transmitter
import threading

#Connection Parameters
UDP_Port = 5005                                         #specifies unused port on network
LOCAL_IP = '0.0.0.0'                                    #specifies IPv4 addresses on the local machine
UDP_IP = '192.168.1.144'                                #target IP address (RasPi)
#ip addr alternate RasPi: 192.168.1.28

#Instantiate modules and run necessary threads
transmit = transmitter(UDP_Port, LOCAL_IP, UDP_IP)
t = threading.Thread(target=transmit.recv_msg)          #thread will handle sending of messages
t.start()                                               #start the additional thread
transmit.send_msg()                                     #start the message sending system on the current thread