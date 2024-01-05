import RPi.GPIO as GPIO
from time import sleep

in1 = 23
in2 = 24
ena = 25

temp1 = 1

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)



GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)

a = GPIO.PWM(ena, 1000)
a.start(75)

def stop(s):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    sleep(s)
def forward(s):
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    sleep(s)
def backward(s):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    sleep(s)


print("ready")
sleep(3)

forward(3)
backward(3)
stop(3)
