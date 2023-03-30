import os
import requests
from dotenv import load_dotenv
from config import Config  # 추가

load_dotenv(verbose=True)

PAPAGO_API_URL = Config.PAPAGO_API_URL  # 수정
client_id = Config.PAPAGO_CLIENT_ID  # 수정
client_secret = Config.PAPAGO_CLIENT_SECRET  # 수정

def translate(text, target='ko'):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    }
    data = {
        'source': 'auto',
        'target': target,
        'text': text
    }
    response = requests.post(PAPAGO_API_URL, headers=headers, data=data).json()
    return response['message']['result']['translatedText']
