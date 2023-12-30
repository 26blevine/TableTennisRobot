import RPi.GPIO as GPIO
from time import sleep
import sys

a = 12
b = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12, GPIO.LOW)
sleep(1)
GPIO.output(12, GPIO.HIGH)
sleep(5)
GPIO.output(12, GPIO.LOW)
GPIO.cleanup()
sys.exit()