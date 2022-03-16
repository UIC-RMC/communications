import tcpModule

ser = tcpModule.protoSerializer()
#update a movement=0 message
ser.updateMovement(555,343)
print(ser.movement.mtr_spd)
print(ser.movement.mtr_ang)
