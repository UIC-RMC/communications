from udpModule import reciever
from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
import threading
import time

controller = RoboteqHandler(debug_mode=True, exit_on_interrupt=False)
connected = controller.connect("/dev/ttyACM0") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.

#Connection Parameters
UDP_Port = 5005                                             #specifies unused port on network
LOCAL_IP = '0.0.0.0'                                        #specifies IPv4 addresses on the local machine
UDP_IP = '192.168.1.162'                                    #target IP address (external)

recieve = reciever(UDP_Port, LOCAL_IP, UDP_IP)
t = threading.Thread(target=recieve.recv_msg)              #specifies that the additional thread will handle recieving messages
t.start()                                                  #start the additional thread

t2 = threading.Thread(target=recieve.send_msg)
t2.start()

def control(x,y):

#motor control parameters: dual_motor_control(motor1, motor2)
    if x<300 and x>-300 and y<300 and y>-300:
        controller.dual_motor_control(0, 0)
        print("Stop")

    if y>=300 and y<=1000 and x>-300 and x<300:
        controller.dual_motor_control(-200, 200)
        print("forward/n")

    elif y<=-300 and y>=-1000 and x>-300 and x<300:
        controller.dual_motor_control(200, -200)
        print("reverse/n")

    elif x>=300 and x<=1000 and y>-300 and y<300:
        controller.dual_motor_control(200, 200)
        print("right/n")

    elif x<=-300 and x>=-1000 and y>-300 and y<300:
        controller.dual_motor_control(-200, -200)
        print("left/n")
    else:
        controller.dual_motor_control(0, 0)
        print("Stop")

while True:
    a = (recieve.msg.split(' '))
    #print(a)
    try:
        x = int(float(a[0]) * 1000)
        y = -1 * int(float(a[1]) * 1000)
        #print(str(x) + ' ' + str(y))
        print(x)
        #print(y)
        control(x,y)

    except:
       pass
    time.sleep(.25)