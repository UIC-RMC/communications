#creator: Alex Domagala

#References:
#https://www.youtube.com/watch?v=fAaxd9MUJcU
#https://stackoverflow.com/questions/33434007/python-socket-send-receive-messages-at-the-same-time
#https://blog.furas.pl/python-socket-send-and-receive-at-the-same-time-gb.html
#https://www.youtube.com/results?search_query=python+threading+library

#turn on sender then the reciever
import socket
import time
import threading
import pygame

pygame.init()
UDP_Port = 5005                                             #specifies unused port on network
LOCAL_IP = '0.0.0.0'                                        #specifies IPv4 addresses on the local machine
UDP_IP = '192.168.1.28'                                     #target IP address (RasPi)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     #permits sending of messages, SOCK_DGRAM = Socket type (UDP)
sock.bind((LOCAL_IP, UDP_Port))                             #permits recieving of messages

def recv_msg():
    while True:
        msg, addr = sock.recvfrom(1024)
        print(msg)

def send_msg():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        axis0 = round(joystick.get_axis(0), 2)
        axis1 = round(joystick.get_axis(1), 2)
        print(axis0)
        sock.sendto(str(axis0), (UDP_IP, UDP_Port))
        time.sleep(.02)

t = threading.Thread(target=recv_msg)                       #specifies that the additional thread will handle recieving messages
t.start()                                                   #start the additional thread
send_msg()                                                  #start the message sending system on the current thread