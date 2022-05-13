import serdes
import tcpModule
import RPi.GPIO as GPIO
import os


while True:
    try:
        #HOST = '192.168.1.162'
        HOST = '0.0.0.0' #special address means "any"
        PORT = 2356

        #monitor pi with GPIO
        LED_PIN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.HIGH)

        #create serializer and reciever objects
        ser = serdes.deserializer()
        print('Waiting to connect!')
        recv = tcpModule.reciever(HOST, PORT)

        #recieve messages
        while True:
            msg = recv.recieve_msg()
            data = ser.decode(msg) #note that data is a python list that contains the different values
            print(data[0]) #contains the message type

            #do the stuff based on the data
            if data[0] == 'move':
                pass

            elif data[0] == 'mine':
                pass

            elif data[0] == 'dump':
                pass
        
    except:
        os.system('tcpReciever.py')