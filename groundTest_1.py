import RPi.GPIO as GPIO
from time import sleep


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
enb_right = 37
#temp_right = 1

outputPins = [17, 27, 22, 5, 6, 13, 23, 24, 25, 12, 16, 37]
inPins = [17, 27, 5, 6, 23, 24, 12, 16]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(outputPins, GPIO.OUT)

a_left = GPIO.PWM(ena_left, 100)
b_left = GPIO.PWM(enb_left, 100)
a_right = GPIO.PWM(ena_right, 100)
b_right = GPIO.PWM(enb_right, 100)

a_left.start(75)
b_left.start(75)
a_right.start(75)
b_right.start(75)

def stop(s):
    GPIO.output(inPins, GPIO.LOW)
    sleep(s)
def forward(s):
    GPIO.output(in1_left, GPIO.HIGH)
    GPIO.output(in2_left, GPIO.LOW)
    GPIO.output(in3_left, GPIO.HIGH)
    GPIO.output(in4_left, GPIO.LOW)

    GPIO.output(in1_right, GPIO.HIGH)
    GPIO.output(in2_right, GPIO.LOW)
    GPIO.output(in3_right, GPIO.HIGH)
    GPIO.output(in4_right, GPIO.LOW)
    sleep(s)
def backward(s):
    GPIO.output(in1_left, GPIO.LOW)
    GPIO.output(in2_left, GPIO.HIGH)
    GPIO.output(in3_left, GPIO.LOW)
    GPIO.output(in4_left, GPIO.HIGH)

    GPIO.output(in1_right, GPIO.LOW)
    GPIO.output(in2_right, GPIO.HIGH)
    GPIO.output(in3_right, GPIO.LOW)
    GPIO.output(in4_right, GPIO.HIGH)
    sleep(s)
def left(s):
    GPIO.output(in1_left, GPIO.HIGH)
    GPIO.output(in2_left, GPIO.LOW)
    GPIO.output(in3_left, GPIO.LOW)
    GPIO.output(in4_left, GPIO.HIGH)

    GPIO.output(in1_right, GPIO.HIGH)
    GPIO.output(in2_right, GPIO.LOW)
    GPIO.output(in3_right, GPIO.LOW)
    GPIO.output(in4_right, GPIO.HIGH)
    sleep(s)
def right(s):
    GPIO.output(in1_left, GPIO.LOW)
    GPIO.output(in2_left, GPIO.HIGH)
    GPIO.output(in3_left, GPIO.HIGH)
    GPIO.output(in4_left, GPIO.LOW)

    GPIO.output(in1_right, GPIO.LOW)
    GPIO.output(in2_right, GPIO.HIGH)
    GPIO.output(in3_right, GPIO.HIGH)
    GPIO.output(in4_right, GPIO.LOW)
    sleep(s)

print("ready")
sleep(15)

forward(3)
backward(3)
left(3)
right(3)
stop(3)
