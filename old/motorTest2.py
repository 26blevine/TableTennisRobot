import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
print(3)
def init():
	print("init")
	gpio.setmode(gpio.BCM)
	gpio.setup(17, gpio.OUT)
	gpio.setup(22, gpio.OUT)
	gpio.setup(23, gpio.OUT)
	gpio.setup(24, gpio.OUT)
	gpio.setup(25, gpio.OUT)
	gpio.setup(12, gpio.OUT)
	gpio.output(17, gpio.LOW)
	gpio.output(22, gpio.LOW)
	gpio.output(23, gpio.LOW)
	gpio.output(24, gpio.LOW)
	a=gpio.PWM(25, 1000)
	#b=gpio.PWM(12, 1000)
	a.start(25)
	#b.start(12)
	
def forward(s):
	init()
	print("forward")
	gpio.output(17, False)
	gpio.output(22, True)
	gpio.output(23, True)
	gpio.output(24, False)
	time.sleep(s)
	
def reverse(s):
	init()
	print("reverse")
	gpio.output(17, True)
	gpio.output(22, False)
	gpio.output(23, False)
	gpio.output(24, True)
	time.sleep(s)
	
def left_turn(s):
	init()
	print("left turn")
	gpio.output(17, True)
	gpio.output(22, False)
	gpio.output(23, True)
	gpio.output(24, False)
	time.sleep(s)
    
def right_turn(s):
	init()
	print("right turn")
	gpio.output(17, False)
	gpio.output(22, True)
	gpio.output(23, False)
	gpio.output(24, True)
	time.sleep(s)

seconds = 3

forward(3)
time.sleep(2)
reverse(3)
time.sleep(2)
left_turn(3)
time.sleep(2)
right_turn(3)
time.sleep(2)
print("done!")
