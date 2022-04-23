#import serdes
import xboxControl as xb
import tcpModule
import serdes
from time import sleep

HOST = ''
PORT = 61626

#create controller object
joy = xb.XboxController()

#create serializer and transmitter objects
ser = serdes.serializer()
#trans = tcpModule.transmitter(HOST, PORT)

#example: we want to send a movement message
#ser.updateMovement(555,352)
#msg = ser.serialize() #msg is the serialized movement command

#send the message every 2 seconds
#if amount greater than delta send new message!

#initialize inputs
Ix = 0
Iy = 0
IdigEnable = 0
IdigAct = 0
IdigVel = 0
IdumpUP = 0
IdumpDOWN = 0

TrackdigEnable = 0

while True:

#MAYBE PUT THIS SECTION INTO A NEW CLASS!
    #controller inputs
    inputs = joy.read()
    x           = inputs[0]
    y           = inputs[1]
    digEnable   = inputs[2]
    digAct      = inputs[3]
    digVel      = inputs[4]
    dumpUP      = inputs[5]
    dumpDOWN    = inputs[6]
    estop       = inputs[7]

    #movement delta ______________FIX UINT32 to make signed integer!!!
    delta = 200
    if (abs(x-Ix) > delta or abs(y-Iy) > delta):
        print('x: ' + str(x))
        print('y: ' + str(y))
        ser.updateMovement(x,y)
        print(ser.serialize())
        Ix = x
        Iy = y

    #digging delta
    delta = 200
    if (digEnable == 1 and IdigEnable != 1):
        if (TrackdigEnable == 0):
            TrackdigEnable = 1
        elif (TrackdigEnable == 1):
            TrackdigEnable = 0
        print('digEnable: ' + str(TrackdigEnable))
        IdigEnable = 1
    elif (digEnable == 0):
        IdigEnable = 0
    if (abs(digAct - IdigAct) > delta):
        print('digAct: ' + str(digAct))
        IdigAct = digAct
    if (abs(digVel - IdigVel) > delta):
        print('digVel:' + str(digVel))
        IdigVel = digVel

    #dumping delta
    if (dumpUP != IdumpUP):
        print('dumpUp: ' + str(dumpUP))
        ser.updateDumping(dumpUP, 0)
        IdumpUP = dumpUP
    if (dumpDOWN != IdumpDOWN):
        print('dumpDOWN: ' + str(dumpDOWN))
        ser.updateDumping(0, dumpDOWN)
        IdumpDOWN = dumpDOWN
    

    #trans.send_msg(msg)
    #sleep(2)