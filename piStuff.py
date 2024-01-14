import requests
import subprocess

#subprocess.Popen('raspistill -n -o ~/Desktop/frame.jpg', shell=True) # dont do this on desktop
# put it in a folder, easier 
# make it save to somewhere good

url = 'http://10.0.0.157:3000/api/send'  # REPLACE THE IP ADRESS W THE ONE I SHOWED
# YOU HOW TO GETTTTTTTTT
files = {'file': open('./pictures/woah.jpg', 'rb')}  # make the path to the folder RELATIVe
# TO WHERE YOU AREEEEEE
# make the ./pictures/waoh whatever make that where the thing pu in the subprocess thing

response = requests.post(url, files=files)
print(response.json())