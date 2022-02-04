#creator: Alex Domagala

#https://www.youtube.com/watch?v=fAaxd9MUJcU
#https://stackoverflow.com/questions/45345730/raspberry-pi-tcp-socket-errno-99-cannot-assign-requested-address

import time
import threading
import socket
import RPi.GPIO as GPIO
import os

#GPIO Test Code
#pin = 3
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM) 
#GPIO.setup(pin,GPIO.OUT)

UDP_Port = 5005                                             #specifies unused port on network
LOCAL_IP = '0.0.0.0'                                        #specifies IPv4 addresses on the local machine
UDP_IP = '192.168.1.162'                                    #target IP address (RasPi)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     #permits sending of messages, SOCK_DGRAM = Socket type (UDP)
sock.bind((LOCAL_IP, UDP_Port))                             #permits recieving of messages

def recv_msg():
    while True:
        msg, addr = sock.recvfrom(1024)
        print(msg)

def send_msg():
    while True:
        v = raw_input()
        MESSAGE = str(v)
        sock.sendto(MESSAGE, (UDP_IP, UDP_Port))

t = threading.Thread(target=recv_msg)                       #specifies that the additional thread will handle recieving messages
t.start()                                                   #start the additional thread
send_msg()                                                  #start the message sending system on the current thread