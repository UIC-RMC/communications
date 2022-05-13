#creator: Alex Domagala
#Module responsible for handling control input collection and sending/recieving data via protoBuffers
#Module uses TCP rather than UDP

#steps: make a new proto file that can package all the command data together
#make class that can actually send the protobuffer data

#https://stackoverflow.com/questions/40450556/how-to-know-which-protobuf-message-the-byte-array-is/50291651#50291651
#https://sureshjoshi.com/development/streaming-protocol-buffers
#https://eli.thegreenplace.net/2011/08/02/length-prefix-framing-for-protocol-buffers
#encode multiple messages

#note that wrapMsg will reflect the data from the function that last updated it

import socket
import cmd_pb2 as pb

class serializer:
    def __init__(self):
        self.wrapMsgEncode = pb.WrapperMessage()
        self.serialized = None

    #note: message type must match the name in the wrapper
    def updateMovement(self, mtr_spd, mtr_ang):
        self.wrapMsgEncode.movement.mtr_spd = mtr_spd
        self.wrapMsgEncode.movement.mtr_ang = mtr_ang

    def updateDumping(self, extend, retract):
        self.wrapMsgEncode.dumping.extend = extend
        self.wrapMsgEncode.dumping.retract = retract

    def updateMining(self, mtr_mining, extend, retract, dig_spd):
        self.wrapMsgEncode.mining.mtr_mining = mtr_mining
        self.wrapMsgEncode.mining.extend = extend
        self.wrapMsgEncode.mining.retract = retract
        self.wrapMsgEncode.mining.dig_spd = dig_spd

    #serialized the message, it can then be sent, idea we can also serialize inside each update method?
    def serialize(self):
        return self.wrapMsgEncode.SerializeToString()

class deserializer():
    def __init__(self):
        self.wrapMsgDecode = pb.WrapperMessage()

    #msg are they bytes sent over TCP
    def decode(self, msg):
        self.wrapMsgDecode.ParseFromString(msg)

        if (self.wrapMsgDecode.HasField('movement')):
            print('Movement Msg Recieved')
            #print(self.wrapMsgDecode.movement.mtr_spd)
            #print(self.wrapMsgDecode.movement.mtr_ang)
            spd = self.wrapMsgDecode.movement.mtr_spd
            ang = self.wrapMsgDecode.movement.mtr_ang
            move = ['move', spd, ang]
            return move

        if (self.wrapMsgDecode.HasField('mining')):
            print('Mining Msg Recieved')
            #print(self.wrapMsgDecode.mining.mtr_mining)
            #print(self.wrapMsgDecode.mining.extend)
            #print(self.wrapMsgDecode.mining.retract)
            #print(self.wrapMsgDecode.mining.dig_spd)
            enable = self.wrapMsgDecode.mining.mtr_mining
            extend = self.wrapMsgDecode.mining.extend
            retract = self.wrapMsgDecode.mining.retract
            dig_spd = self.wrapMsgDecode.mining.dig_spd
            mine = ['mine', enable, extend, retract, dig_spd]
            return mine

        if (self.wrapMsgDecode.HasField('dumping')):
            print('Dumping Msg Recieved')
            #print(self.wrapMsgDecode.dumping.extend)
            #print(self.wrapMsgDecode.dumping.retract)
            extend = self.wrapMsgDecode.dumping.extend
            retract = self.wrapMsgDecode.dumping.retract
            dump = ['dump', extend, retract]
            return dump