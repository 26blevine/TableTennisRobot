import requests

def piTransfer3():
    print('3')
    #response = requests.get('http://192.168.1.27:3000/api/get_data')
    response = requests.get('http://192.168.1.18:3000/api/get_data')
    rj = response.json()
    values = rj['result']
    print(response.json())