import requests
from django.conf import settings


def send_otp_code(phone_number, code):
    url = 'https://api.limosms.com/api/sendpatternmessage'
    message = [f"{code}"]
    myobj = {'OtpId' :'593',
    'ReplaceToken' : message,
    'MobileNumber' : f'{phone_number}'}
    x = requests.post(url, json = myobj, headers = {"ApiKey": settings.API_KEY})
    print(x.text)