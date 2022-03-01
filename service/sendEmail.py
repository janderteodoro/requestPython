import requests 

def sendMail(url, payload): 
    re = requests.post(url , data=payload)
    return re.json()