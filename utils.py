import requests
from django.conf import settings


def send_otp_code(phone_number, code):
    url = 'https://api.limosms.com/api/sendcode'
    myobj = {'Mobile' :f'{phone_number}',
    'Footer' : f'{code}کد تایید شما'}
    x = requests.post(url, json = myobj, headers = {"ApiKey":settings.API_KEY})
    print(x.text)
