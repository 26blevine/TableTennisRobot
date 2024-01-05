import RPi.GPIO as GPIO
from time import sleep
import sys


# Left front
in1_left = 17
in2_left = 27
ena_left = 22
# Left back
in3_left = 5
in4_left = 6
enb_left = 13
#temp_left = 1

# Right back
in1_right = 23
in2_right = 24
ena_right = 25
# Right front
in3_right = 12
in4_right = 16
enb_right = 26
#temp_right = 1

outputPins = [17, 27, 22, 5, 6, 13, 23, 24, 25, 12, 16, 26]
inPins = [17, 27, 5, 6, 23, 24, 12, 16]

GPIO.setmode(GPIO.BCM)
GPIO.setup(outputPins, GPIO.OUT)

a_left = GPIO.PWM(ena_left, 100)
b_left = GPIO.PWM(enb_left, 100)
a_right = GPIO.PWM(ena_right, 100)
b_right = GPIO.PWM(enb_right, 100)

a_left.start(0)
b_left.start(0)
a_right.start(0)
b_right.start(0)

def stop(s):
    GPIO.output(inPins, GPIO.LOW)

    sleep(s)
def forward(s):
    print("forwards")
    GPIO.output(in1_left, GPIO.HIGH)
    GPIO.output(in2_left, GPIO.LOW)
    GPIO.output(in3_left, GPIO.HIGH)
    GPIO.output(in4_left, GPIO.LOW)

    GPIO.output(in1_right, GPIO.HIGH)
    GPIO.output(in2_right, GPIO.LOW)
    GPIO.output(in3_right, GPIO.HIGH)
    GPIO.output(in4_right, GPIO.LOW)


    a_right.ChangeDutyCycle(100)
    b_right.ChangeDutyCycle(100)
    a_left.ChangeDutyCycle(100)
    b_left.ChangeDutyCycle(100)

    sleep(s)

def backward(s):
    print("backwards")
    GPIO.output(in1_left, GPIO.LOW)
    GPIO.output(in2_left, GPIO.HIGH)
    GPIO.output(in3_left, GPIO.LOW)
    GPIO.output(in4_left, GPIO.HIGH)

    GPIO.output(in1_right, GPIO.LOW)
    GPIO.output(in2_right, GPIO.HIGH)
    GPIO.output(in3_right, GPIO.LOW)
    GPIO.output(in4_right, GPIO.HIGH)

    a_right.ChangeDutyCycle(100)
    b_right.ChangeDutyCycle(100)
    a_left.ChangeDutyCycle(100)
    b_left.ChangeDutyCycle(100)

    sleep(s)

def right(s):
    print("right")
    GPIO.output(in1_left, GPIO.HIGH)
    GPIO.output(in2_left, GPIO.LOW)
    GPIO.output(in3_left, GPIO.HIGH)
    GPIO.output(in4_left, GPIO.LOW)

    GPIO.output(in1_right, GPIO.LOW)
    GPIO.output(in2_right, GPIO.HIGH)
    GPIO.output(in3_right, GPIO.LOW)
    GPIO.output(in4_right, GPIO.HIGH)

    a_right.ChangeDutyCycle(100)
    b_right.ChangeDutyCycle(100)
    a_left.ChangeDutyCycle(100)
    b_left.ChangeDutyCycle(100)

    sleep(s)

def left(s):
    print("left")
    GPIO.output(in1_left, GPIO.LOW)
    GPIO.output(in2_left, GPIO.HIGH)
    GPIO.output(in3_left, GPIO.LOW)
    GPIO.output(in4_left, GPIO.HIGH)

    GPIO.output(in1_right, GPIO.HIGH)
    GPIO.output(in2_right, GPIO.LOW)
    GPIO.output(in3_right, GPIO.HIGH)
    GPIO.output(in4_right, GPIO.LOW)

    a_right.ChangeDutyCycle(100)
    b_right.ChangeDutyCycle(100)
    a_left.ChangeDutyCycle(100)
    b_left.ChangeDutyCycle(100)

    sleep(s)

print("ready")

#sleep(5)
'''
forward(3)
backward(3)
left(3)
right(3)
stop(3)
'''
isStopped = False
while not isStopped:
	inp = input("operation: ")
	if (inp  == "f"):
		forward(3)
	elif (inp == "b"):
		backward(3)
	elif (inp == "l"):
		left(3)
	elif (inp == "r"):
		right(3)
	elif (inp == "s"):
		stop(3)
	elif (inp == "e"):
		isStopped = True
		GPIO.cleanup()
		sys.exit()
	else:
		print("Invalid ")
