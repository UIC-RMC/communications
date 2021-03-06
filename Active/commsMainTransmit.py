from udpModule import transmitter
import threading

#Connection Parameters
UDP_Port = 5005                                             #specifies unused port on network
LOCAL_IP = '0.0.0.0'                                        #specifies IPv4 addresses on the local machine
UDP_IP = '192.168.1.144'                                    #target IP address (RasPi)

#MAIN
transmit = transmitter(UDP_Port, LOCAL_IP, UDP_IP)
t = threading.Thread(target=transmit.recv_msg)              #specifies that the additional thread will handle recieving messages
t.start()                                                   #start the additional thread
transmit.send_msg()                                         #start the message sending system on the current thread