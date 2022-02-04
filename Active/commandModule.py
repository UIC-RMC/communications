#creator: Alex Domagala
#Module responsible for handling movement of the robot

from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds

class movementControl:
    def __init__(self):

        #Link to Roboteq motor controller
        self.controller = RoboteqHandler(debug_mode=True, exit_on_interrupt=False)
        self.connected = self.controller.connect("/dev/ttyACM0") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.

    def move(self, x, y):
        
        #control parameters: dual_motor_control(motor1, motor2)
        if (x < 300 and x > -300 and y < 300 and y > -300):
            self.controller.dual_motor_control(0, 0)
            print("Stop")

        if (y >= 300 and y <= 1000 and x > -300 and x < 300):
            self.controller.dual_motor_control(-200, 200)
            print("forward/n")

        elif (y <= -300 and y >= -1000 and x > -300 and x < 300):
            self.controller.dual_motor_control(200, -200)
            print("reverse/n")

        elif (x >= 300 and x <= 1000 and y > -300 and y < 300):
            self.controller.dual_motor_control(200, 200)
            print("right/n")

        elif (x <= -300 and x >= -1000 and y > -300 and y < 300):
            self.controller.dual_motor_control(-200, -200)
            print("left/n")
        
        else:
            self.controller.dual_motor_control(0, 0)
            print("Stop")