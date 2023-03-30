import sys
import os
from flask import Flask, render_template, request
from modules.papago import translate
from modules.chatGPT import generate_answer
from modules.polly import synthesize_speech

app = Flask(__name__)

# 모듈 경로 추가
sys.path.append(os.path.abspath('./modules'))

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
    return {'question': question, 'answer': answer, 'translated_question': translated_question, 'translated_answer': translated_answer, 'speech': speech}

if __name__ == '__main__':
    app.run(debug=True)
