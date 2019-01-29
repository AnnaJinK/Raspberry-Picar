import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

ENA = 33
pin1 = 35
pin2 = 37

GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

pin3 = 36
pin4 = 38
ENB = 40

GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

# RIGHT MOTOR
def rForward():
    print('r_Forward')
    GPIO.output(ENA, 1)
    GPIO.output(pin1, 0)
    GPIO.output(pin2, 1)

def rBackward():
    print('r_Backward')
    GPIO.output(ENA, 1)
    GPIO.output(pin1, 1)
    GPIO.output(pin2, 0)

#LEFT MOTOR
def lForward():
    print('l_Forward')
    GPIO.output(ENB, 1)
    GPIO.output(pin3, 0)
    GPIO.output(pin4, 1)

def lBackward():
    print('l_Backward')
    GPIO.output(ENB, 1)
    GPIO.output(pin3, 1)
    GPIO.output(pin4, 0)

# MOTOR STOP
def Stop():
    print('Stop')
    GPIO.output(ENA, 0)
    GPIO.output(ENB, 0)

#rForward()
#time.sleep(0.5)
#rBackward()
#time.sleep(0.5)
#Stop()
lForward()
time.sleep(1)
lBackward()
time.sleep(1)
Stop()
pwm_fan = GPIO.PWM(ENA, 100)
pwm_fan.start(0)
pwm_motor = GPIO.PWM(ENB, 100)
pwm_motor.start(0)

try:
    while True:
        gear = int(input("Press gear(0, 1, 2, 3) : "))
        if gear == 0:
            print('Gear 0')
            pwm_motor.ChangeDutyCycle(0)
            pwm_fan.ChangeDutyCycle(0)
        elif gear == 1:
            print('Gear 1')
            pwm_motor.ChangeDutyCycle(100)
        elif gear == 2:
            print('Gear 2')
            rBackward()
            pwm_fan.ChangeDutyCycle(30)
        elif gear == 3:
            print('Gear 3')
            rForward()
            pwm_fan.ChangeDutyCycle(10)
        elif gear == 4:
            print('Gear 4')
            rForward()
            pwm_fan.ChangeDutyCycle(20)
        elif gear == 5:
            print('Gear 5')
            rForward()
            pwm_fan.ChangeDutyCycle(30)
        else:
            print('fuck!')
finally:
    print('Clean')
    GPIO.cleanup()






