from flask import Flask, render_template, request, jsonify, send_from_directory
from dotenv import load_dotenv
import os
from modules.papago_api import translate_text
from modules.chatgpt_api import get_chatgpt_response
from modules.polly_api import text_to_speech

load_dotenv()

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.json['text']
    translated_text = translate_text(text)
    return jsonify(translated_text=translated_text)

@app.route('/chat', methods=['POST'])
def chat():
    text = request.json['text']
    source_lang = 'ko'
    target_lang = 'en'
    translated_text = translate_text(text, source_lang, target_lang)
    chatgpt_response = get_chatgpt_response(translated_text)
    translated_chatgpt_response = translate_text(chatgpt_response, target_lang, source_lang)
    return jsonify(chatgpt_response=translated_chatgpt_response)

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.json['text']
    audio_url = text_to_speech(text)
    return jsonify(audio_url=audio_url)

if __name__ == '__main__':
    app.run(debug=True)
