import requests
def piTransfer2():
    url = 'http://192.168.1.27:3000/api/send'  # REPLACE THE IP ADRESS W THE ONE I SHOWED
    # YOU HOW TO GETTTTTTTTT
    files = {'file': open('./pictures/frame.jpg', 'rb')}  # make the path to the folder RELATIVe
    # TO WHERE YOU AREEEEEE
    # make the ./pictures/waoh whatever make that where the thing pu in the subprocess thing

    response = requests.post(url, files=files)
    print(response.json())
    
    
    