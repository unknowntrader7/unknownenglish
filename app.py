from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import papago_api
import chatgpt_api
import polly_api

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.json['text']
    translated_text = papago_api.translate(text)
    return jsonify(translated_text=translated_text)

@app.route('/chat', methods=['POST'])
def chat():
    text = request.json['text']
    chatgpt_response = chatgpt_api.get_chatgpt_response(text)
    return jsonify(chatgpt_response=chatgpt_response)

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.json['text']
    audio_url = polly_api.synthesize_speech(text)
    return jsonify(audio_url=audio_url)

if __name__ == '__main__':
    app.run(debug=True)
    