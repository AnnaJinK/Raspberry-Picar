from subprocess import call
import time

#print('servo test')
#for i in range(1,6):
#    call("echo 1="+str(i*50)+" > /dev/servoblaster", shell=True)
#    time.sleep(1)
#for i in range(5,0,-1):
#    call("echo 1="+str(i*50)+" > /dev/servoblaster", shell=True)
#    time.sleep(1)

call("sudo pigpiod", shell=True)
time.sleep(0.2)
print("start pigpiod")
call("sudo ds4drv", shell=True)
time.sleep(0.2)
print("start ds4drv")

#while True:
  #  call("echo 1=150 > /dev/servoblaster", shell=True)
    #position = raw_input("Enter servo value :")
    #call("echo 1="+position+" > /dev/servoblaster", shell=True)
    #time.sleep(1)
