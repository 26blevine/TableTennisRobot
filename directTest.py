import RPi.GPIO as GPIO
from time import sleep
import sys

a = 12
b = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
print("setup")
GPIO.output(12, GPIO.LOW)
sleep(1)
print("on")
GPIO.output(12, GPIO.HIGH)
sleep(5)
print("off")
GPIO.output(12, GPIO.LOW)
GPIO.cleanup()
sys.exit()
