import requests

def piTransfer3():
    #response = requests.get('http://192.168.1.27:3000/api/get_data')
    response = requests.get('http://192.168.1.27:3000/api/get_data')

    print(response.json())