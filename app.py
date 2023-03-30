from flask import Flask, render_template, request, jsonify, send_from_directory
from dotenv import load_dotenv
import os
import modules.papago_api as papago_api
import modules.chatgpt_api as chatgpt_api
import modules.polly_api as polly_api

load_dotenv()

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return rende_template('index.html')

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
