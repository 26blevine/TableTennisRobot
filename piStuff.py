import requests

url = 'http://192.168.1.27:5000/api/send'  # Replace with the correct URL if needed
files = {'file': open('.~/Desktop/frame.jpg', 'rb')}  # Replace with your file path

response = requests.post(url, files=files)
print(response.json())