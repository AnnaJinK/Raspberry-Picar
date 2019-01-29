"""
start program
"""

from subprocess import call
import time

print("pigpiod load")
call("lxterminal -e sudo pigpiod", shell=True)
time.sleep(2)
print("ds4drv load")
call("lxterminal -e sudo ds4drv", shell=True)
time.sleep(10)
call('lxterminal -e python3 /home/pi/Desktop/PiCar/car/rc.py', shell=True) # "&"background process
print("online")
