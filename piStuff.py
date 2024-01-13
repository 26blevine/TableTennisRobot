import requests
import subprocess

subprocess.Popen('raspistill -n -o ~/Desktop/frame.jpg', shell=True)

url = 'http://192.168.1.27:5000/api/send'  # Replace with the correct URL if needed
files = {'file': open('   frame.jpg', 'rb')}  # Replace with your file path

response = requests.post(url, files=files)
print(response.json())