from udpModule import reciever
import threading
import time

#Connection Parameters
UDP_Port = 5005                                             #specifies unused port on network
LOCAL_IP = '0.0.0.0'                                        #specifies IPv4 addresses on the local machine
UDP_IP = '192.168.1.162'                                    #target IP address (RasPi)

recieve = reciever(UDP_Port, LOCAL_IP, UDP_IP)
t = threading.Thread(target=recieve.recv_msg)              #specifies that the additional thread will handle recieving messages
t.start()                                                   #start the additional thread

t2 = threading.Thread(target=recieve.send_msg)
t2.start()

while True:
    a = (recieve.msg.split(' '))
    #print(a)
    try:
        x = int(float(a[0]) * 1000)
        y = -1 * int(float(a[1]) * 1000)
        #print(str(x) + ' ' + str(y))
        #print(x)
        print(y)
    except:
       pass
    time.sleep(.25)