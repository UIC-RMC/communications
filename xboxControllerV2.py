#creator: Alex Domagala

#https://www.pygame.org/docs/ref/joystick.html

import pygame
from time import sleep
pygame.init()
while True:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
    #print("I'm a main loop")
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    name = joystick.get_name()
    # print("Joystick name: {}".format(name) )
    axes = joystick.get_numaxes()

    # pygame.joystick.Joystick.get_axis
    #pick your axis here!!!
    axis0 = joystick.get_axis(0)
    axis1 = joystick.get_axis(1)

    print("Axis {} value: {:>6.3f}".format(0, axis0))
    #print("Axis {} value: {:>6.3f}".format(1, axis1))
    sleep(.02)

#axis(0): x-axis for the left stick
#axis(1): y-axis for the left stick
#-1 is left or up
#+1 is right or down