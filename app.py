import os
from flask import Flask, render_template, request, jsonify
from modules.papago_api import translate
from modules.chatgpt_api import get_chatgpt_response
from modules.polly_api import synthesize_speech

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_answer', methods=['POST'])
def get_answer():
    question = request.form['question']
    lang = request.form['lang']
    translated_question = translate(question, lang)
    answer = generate_answer(translated_question)
    translated_answer = translate(answer, 'ko')
    speech = synthesize_speech(answer)
    return jsonify({'question': question, 'answer': answer, 'translated_question': translated_question, 'translated_answer': translated_answer, 'speech': speech})

if __name__ == '__main__':
    app.run(debug=True)
