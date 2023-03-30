import requests
import os

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

def translate_text(text, source_lang='ko', target_lang='en'):
    url = "https://openapi.naver.com/v1/papago/n2mt"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }
    data = {
        "source": source_lang,
        "target": target_lang,
        "text": text
    }
    response = requests.post(url, headers=headers, data=data)
    translated_text = response.json()["message"]["result"]["translatedText"]
    return translated_text
