import math
import cv2
from roboflow import Roboflow

class objectBox:
    def __init__(this, t, b, l, r):
        this.top = t
        this.bottom = b
        this.left = l
        this.right = r

        this.x_center = (this.left+this.right)/2
        this.y_center = (this.top+this.bottom)/2

        this.x_dist = this.x_center - 320
        this.y_dist = 480-this.y_center
        this.absolute_distance = math.hypot(this.x_dist, this.y_dist)
    def __repr__(this):
        return f"abs {this.absolute_distance}, top {this.top}, bottom {this.bottom}, left {this.left}, right {this.right}"
    def getAbsoluteDistance(this):
        return this.absolute_distance
# Roboflow Model Importing
rf = Roboflow(api_key="iyABRjJ0CKFV2IT0liyK")
project = rf.workspace("bsl").project("table-tennis-ball-model")
dataset = project.version(1).download("yolov5")
model = project.version(1).model
# Video Capture Setup
webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cv2.namedWindow("Live View", cv2.WINDOW_NORMAL)

leftMotors = 1
rightMotors = 1

print("Setup Complete!")

def analyzeFrame(imagePath):
    # Take Frame From Webcam
    print("New Frame")
   # result, frame = webcam.read()
    # Choose Frame To Investigate
    imageCaptured = imagePath
    # Predict
    prediction = model.predict(imageCaptured)
    #Initialize list
    ballsFound = []
    # Calculate boundaries for bounding box
    for bounding_box in prediction:
        x1 = bounding_box['x'] - bounding_box['width'] / 2
        x2 = bounding_box['x'] + bounding_box['width'] / 2
        y1 = bounding_box['y'] - bounding_box['height'] / 2
        y2 = bounding_box['y'] + bounding_box['height'] / 2
        # Create bounding box object
        ballBox = objectBox(x1, x2, y1, y2)
        #add bounding box to list
        ballsFound.append(ballBox)
        #print(ballBox.absolute_distance)



    #print("Unsorted:")
    #print(ballsFound)
    ballsFound.sort(key=lambda objectBox: objectBox.absolute_distance)
    #print("Sorted")
    #print(ballsFound)
    prediction.plot()
    closestBall = ballsFound[0]
    closestBall_dist = [closestBall.x_dist, closestBall.y_dist, closestBall.absolute_distance]
    #print(f"The closest ball is {closestBall.absolute_distance} pixels away")
    print(f"x: {closestBall_dist[0]}, y: {closestBall_dist[1]}, abs: {closestBall_dist[2]}")
    analyzeDistance(closestBall_dist[0], closestBall_dist[1], closestBall_dist[2])

'''
    if closestBall.x_dist > 25:
        leftMotors = 1
        rightMotors = 0
    elif closestBall.x_dist < -25:
        leftMotors = 0
        rightMotors = 1
    else:
        leftMotors = 1
        rightMotors = 1
'''
def analyzeDistance(x, y, abs):
    x_dist = x
    y_dist = y
    abs_dist = abs