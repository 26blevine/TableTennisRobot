import subprocess
from time import sleep
def cam():
#     print('test')
    print('1')
    subprocess.Popen('rpicam-still --timeout 1000 --output /home/benjylevine/Downloads/robot/frame/frame.jpg', shell=True) # dont do this on desktop
    sleep(5)
    print('test over')
# put it in a folder, easier 
# make it save to somewhere good

cam()
