import requests

response = requests.get('http://192.168.1.27:3000/api/get_data')
print(response.json())