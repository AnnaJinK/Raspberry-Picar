#!/usr/bin/env python
from subprocess import call
import time

print("ds4drv load")
call("sudo /usr/local/bin/ds4drv &", shell=True)
time.sleep(10)
print("pigpiod load")
call("lxterminal -e sudo /usr/bin/pigpiod", shell=True)
time.sleep(2)
call('lxterminal -e /usr/bin/python3 /home/pi/rc.py &', shell=True) # "&"background process
print("online")
