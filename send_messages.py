import requests
import json
def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'FIND_YOUR_OWN',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    #print(dic)
    return dic.get('return')


num = int(input("Enter The Number:\n"))
msg = input("Enter The Message You Want To Send:\n")
s = send_sms(num, msg)
if s:
    print("Successfully sent")
else:
    print("Something went wrong..")