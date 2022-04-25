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
trans = tcpModule.transmitter(HOST, PORT)

#initialize inputs
Ix = 0
Iy = 0
IdigEnable = 0
IdigAct = 0
IdigVel = 0
IdumpUP = 0
IdumpDOWN = 0

#state variable
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

    #Emergency Stop
    if (estop == 1):
        print('estop')
        #ser.updateMovement(0,0)
        #trans.send_msg(ser.serialize())
        #ser.updateMining(0, 0, 0, 0)
        #trans.send_msg(ser.serialize())
        #ser.updateDumping(0, 0)
        #trans.send_msg(ser.serialize())
        continue


#movement delta (delta can be used to adjust how much we want to sent) -- COMPLETE
    delta = 50
    if (abs(x-Ix) > delta or abs(y-Iy) > delta):
        print('x: ' + str(x) + ', y: ' + str(y))
        ser.updateMovement(x,y)
        trans.send_msg(ser.serialize())
        Ix = x
        Iy = y

#digging delta

    #digging enable/disable (actuators are not extending or retracting)
    if (digEnable == 1 and IdigEnable != 1):
        if (TrackdigEnable == 0):
            TrackdigEnable = 1
        elif (TrackdigEnable == 1):
            TrackdigEnable = 0

        print('digEnable: ' + str(TrackdigEnable))
        ser.updateMining(TrackdigEnable, 0, 0, digVel)
        trans.send_msg(ser.serialize())
        IdigEnable = 1

    elif (digEnable == 0):
        IdigEnable = 0

    #digging actuator extend/retract: extend = 1, retract = 0
    if (digAct > 0 and digAct != IdigAct):
        print('extendAct: ' + str(1))
        ser.updateMining(TrackdigEnable, 1, 0, digVel)
        trans.send_msg(ser.serialize()) #MAYBE MOVE TO THE END OF THE DIGGING SECTION?
        IdigAct = digAct
    elif (digAct < 0 and digAct != IdigAct):
        print('retractAct: ' + str(-1))
        ser.updateMining(TrackdigEnable, 0, 1, digVel)
        trans.send_msg(ser.serialize())
        IdigAct = digAct

    elif (digAct == 0 and digAct != IdigAct):
        print('zeroAct: ' + str(0))
        ser.updateMining(TrackdigEnable, 0, 0, digVel)
        trans.send_msg(ser.serialize())
        IdigAct = digAct

    #digging motor velocity
    delta = 100
    if (abs(digVel - IdigVel) > delta):
        print('digVel:' + str(digVel))
        ser.updateMining(TrackdigEnable, 0, 0, digVel)
        trans.send_msg(ser.serialize())
        IdigVel = digVel

#dumping delta
    if (dumpUP != IdumpUP):
        print('dumpUp: ' + str(dumpUP))
        ser.updateDumping(dumpUP, 0)
        trans.send_msg(ser.serialize())
        IdumpUP = dumpUP
    if (dumpDOWN != IdumpDOWN):
        print('dumpDOWN: ' + str(dumpDOWN))
        ser.updateDumping(0, dumpDOWN)
        trans.send_msg(ser.serialize())
        IdumpDOWN = dumpDOWN