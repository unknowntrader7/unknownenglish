import openai
import os
from dotenv import load_dotenv

load_dotenv()

async def get_chatgpt_response(prompt):
    api_key = os.getenv('OPENAI_API_KEY')
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    chatgpt_response = response.choices[0].text.strip()
    return chatgpt_response
