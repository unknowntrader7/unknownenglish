import openai_secret_manager
import openai
from dotenv import load_dotenv
import os

load_dotenv()

# Load OpenAI API key from environment variable or secrets manager
if "openai" in os.environ:
    api_key = os.environ["openai"]
else:
    api_key = openai_secret_manager.get_secret("openai")["api_key"]

# Initialize OpenAI API client
openai.api_key = api_key


def generate_answer(question):
    """
    Generate answer from the given question using GPT-3 model.

    Args:
        question (str): Input question string.

    Returns:
        str: Generated answer string.
    """
    prompt = f"Answer the following question:\nQ: {question}\nA:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        n = 1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer = response.choices[0].text.strip()
    return answer
