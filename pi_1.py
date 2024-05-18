import subprocess

def piTransfer1():
    subprocess.Popen('libcamera-jpeg -t 0 -n -o ./frame.jpg', shell=True) # dont do this on desktop
# put it in a folder, easier 
# make it save to somewhere good
