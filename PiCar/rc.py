#!/usr/bin/env python3
from subprocess import call
call("sudo pigpiod", shell=True)
import time
import pigpio
import pygame
import RPi.GPIO as GPIO
import math

pi = pigpio.pi()
GPIO.setmode(GPIO.BOARD)

SERVO = 4
ESC_GPIO = 17

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

pygame.init()

#Loop until the user clicks the close button.
done = False

# Initialize the joysticks
pygame.joystick.init()
print("PiCar Online")
# -------- Main Program Loop -----------
while done==False:
    
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            if joystick.get_button(0):
                print("square pressed")
            elif joystick.get_button(1):
                print("cross pressed")
            elif joystick.get_button(2):
                print("circle pressed")
            elif joystick.get_button(3):
                print("triangle pressed")
            elif joystick.get_button(4):
                print("L1 pressed")
            elif joystick.get_button(5):
                print("R1 pressed")
            elif joystick.get_button(6):
                print("L2 pressed")
            elif joystick.get_button(7):
                print("R2 pressed")
            elif joystick.get_button(8):
                print("SHARE pressed")
            elif joystick.get_button(9):
                print("OPTIONS pressed")
            elif joystick.get_button(10):
                print("left Axis pressed")
            elif joystick.get_button(11):
                print("right Axis pressed")
            elif joystick.get_button(12):
                print("PS pressed")
            elif joystick.get_button(13):
                print("Touch pad pressed")
        
    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        # SERVO MOTOR
        MAX = 1725
        MID = 1425
        MIN = 1125
        #print(joystick.get_axis(2))
        position = ((-joystick.get_axis(2))*300+MID)
        if position < MIN:
            position = MIN
        elif position > MAX:
            position = MAX
        if MIN <= position <= MAX:
            #print(position)
             pi.set_servo_pulsewidth(SERVO, position)
            #call("echo 1="+str(position)+" > /dev/servoblaster", shell=True)
        # SERVO MOTOR END

        # MOTOR Control
        power = (-joystick.get_axis(1))*50
        
        if joystick.get_axis(1)< -0.1:
            ESC_POWER  = 1520+power
            pi.set_servo_pulsewidth(ESC_GPIO, ESC_POWER)
        elif joystick.get_axis(1)> 0.1:
            ESC_POWER = 1340+power
            pi.set_servo_pulsewidth(ESC_GPIO, ESC_POWER)
        else:
            pi.set_servo_pulsewidth(ESC_GPIO, 0)
        #MOTOR End

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
GPIO.cleanup()
