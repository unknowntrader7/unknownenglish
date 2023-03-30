from flask import Flask, render_template, request, jsonify
import openai
from config import Config
import requests

app = Flask(__name__)
openai.api_key = Config.API_KEY

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        translated_prompt = translate(prompt, "ko", "en")
        response = get_gpt_response(translated_prompt)
        translated_response = translate(response, "en", "ko")
        return jsonify({"response": translated_response})

    return render_template("index.html")

def get_gpt_response(prompt):
    model_engine = "text-davinci-002"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def translate(text, source_lang, target_lang):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Naver-Client-Id": Config.PAPAGO_API_KEY["client_id"],
        "X-Naver-Client-Secret": Config.PAPAGO_API_KEY["client_secret"],
    }
    data = {
        "source": source_lang,
        "target": target_lang,
        "text": text,
    }
    response = requests.post(Config.PAPAGO_API_URL, headers=headers, data=data)
    translated_text = response.json()["message"]["result"]["translatedText"]
    return translated_text

if __name__ == "__main__":
    app.run(debug=True)
