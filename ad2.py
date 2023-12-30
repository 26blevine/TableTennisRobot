
# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep
import sys
in1 = 24
in2 = 23
en = 26
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(12,GPIO.LOW)
GPIO.output(16,GPIO.LOW)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

GPIO.output(16, GPIO.HIGH)
GPIO.output(26, GPIO.HIGH)
sleep(10)
GPIO.cleanup()
sys.exit()