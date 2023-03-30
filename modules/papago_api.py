import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

async def translate(text):
    client_id = os.getenv('PAPAGO_CLIENT_ID')
    client_secret = os.getenv('PAPAGO_CLIENT_SECRET')

    url = 'https://naveropenapi.apigw.ntruss.com/nmt/v1/translation'
    headers = {
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    }
    data = {
        'source': 'en',
        'target': 'ko',
        'text': text
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as resp:
            response = await resp.json()

    translated_text = response['message']['result']['translatedText']
    return translated_text
