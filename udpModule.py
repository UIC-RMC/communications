#creator: Alex Domagala

import socket
import time
import pygame
pygame.init()

UDP_Port = 5005                                             #specifies unused port on network
LOCAL_IP = '0.0.0.0'                                        #specifies IPv4 addresses on the local machine
UDP_IP = '192.168.1.144'                                    #target IP address (RasPi)
#IP OF OTHER PI 192.168.1.28!

class transmitter:
    def __init__(self, UDP_Port, LOCAL_IP, UDP_IP):
        self.UDP_Port = UDP_Port
        self.LOCAL_IP = LOCAL_IP
        self.UDP_IP = UDP_IP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     #permits sending of messages, SOCK_DGRAM = Socket type (UDP)
        self.sock.bind((self.LOCAL_IP, UDP_Port))                        #permits recieving of messages

    def recv_msg(self):
        while True:
            msg, addr = self.sock.recvfrom(1024)
            print(msg)

    def send_msg(self):
        axisXprev = 0
        axisYprev = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            axisX = round(joystick.get_axis(0), 2)
            axisY = round(joystick.get_axis(1), 2)

            #only send the message if we have a change in our controller input
            if (abs(axisXprev-axisX) >= .02) or (abs(axisYprev-axisY) >= .02):
                msg1 = str(axisX) + ' X'
                msg2 = str(axisY) + ' Y'
                
                print(msg1)
                print(msg2)

                self.sock.sendto(msg1, (self.UDP_IP, self.UDP_Port))
                self.sock.sendto(msg2, (self.UDP_IP, self.UDP_Port))

            #storing the comparison values (this is done regardless)
            axisXprev = axisX
            axisYprev = axisY
            time.sleep(.02)

class reciever:
    def __init__(self, UDP_Port, LOCAL_IP, UDP_IP):
            self.UDP_Port = UDP_Port
            self.LOCAL_IP = LOCAL_IP
            self.UDP_IP = UDP_IP
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                #permits sending of messages, SOCK_DGRAM = Socket type (UDP)
            self.sock.bind((self.LOCAL_IP, self.UDP_Port))                              #permits recieving of messages
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                #permits sending of messages, SOCK_DGRAM = Socket type (UDP)
            self.sock.bind((self.LOCAL_IP, self.UDP_Port))                              #permits recieving of messages

    def recv_msg(self):
        while True:
            msg, addr = self.sock.recvfrom(1024)
            print(msg)

    def send_msg(self):
        while True:
            v = input()
            MESSAGE = str(v)
            self.sock.sendto(MESSAGE, (self.UDP_IP, self.UDP_Port))




#t = threading.Thread(target=recv_msg)                       #specifies that the additional thread will handle recieving messages
#t.start()                                                   #start the additional thread
#send_msg()                                                  #start the message sending system on the current thread