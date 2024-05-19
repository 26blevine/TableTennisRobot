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

# Right back
in1_right = 23
in2_right = 24
ena_right = 25
# Right front
in3_right = 12
in4_right = 16
enb_right = 26

#intake
in1_intake = 9
in2_intake = 10
ena_intake = 11


outputPins = [in1_left, in2_left, ena_left, in1_right, in2_right, ena_right, in3_left, in4_left, enb_left, in3_right, in4_right, enb_right, in1_intake, in2_intake, ena_intake]
inPins = [in1_left, in2_left, in1_right, in2_right, in3_left, in4_left, in3_right, in4_right, in1_intake, in2_intake]

GPIO.setmode(GPIO.BCM)
GPIO.setup(outputPins, GPIO.OUT)

a_left = GPIO.PWM(ena_left, 100)
b_left = GPIO.PWM(enb_left, 100)
a_right = GPIO.PWM(ena_right, 100)
b_right = GPIO.PWM(enb_right, 100)
a_intake = GPIO.PWM(ena_intake, 100)

a_left.start(0)
b_left.start(0)
a_right.start(0)
b_right.start(0)
a_intake.start(0)

def stop(s):
    print("stop")
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
    
def cleanup():
    GPIO.cleanup()
    sys.exit()

def intakeIn(s):
    GPIO.output(in1_intake, GPIO.LOW)
    GPIO.output(in2_intake, GPIO.HIGH)
    ena_intake.ChangeDutyCycle(100)
    sleep(s)
def intakeOut(s):
    GPIO.output(in1_intake, GPIO.HIGH)
    GPIO.output(in2_intake, GPIO.LOW)
    ena_intake.ChangeDutyCycle(0)
    sleep(s)

print("ready")

def move(ballCoords):
    x = ballCoords[0]
    y=ballCoords[1]
    abs = ballCoords[2]


    if y != -1:
        x /= 100
        y /= 100

        if x < 0:
            left(int(x))
        else:
            right(int(x))

        forward(int(y))
    else:
        left(int(x))