from flask import Flask, jsonify, render_template, url_for
"""
export FLASK_APP=dream_big.py
export FLASK_ENV=development
flask run
"""

app = Flask(__name__)

boy_dreams = {
        'andy': 'be a superman',
        'jerry': 'be a billionaire',
        'jiaze': 'be a hero',
        'zijun': 'save the world',
        'ranran': 'live in mars',
    }


@app.route('/boys')
def all_boys():
    return jsonify('andy', 'jerry', 'jiaze', 'zijun', 'ranran')


@app.route('/boys/<name>')
def boy(name):
    return boy_dreams[name]


@app.route('/')
def index_page():
    return render_template('dream-big.html')


@app.route('/dream/<name>')
def dream_page(name):
    return render_template('my-dream.html', name=name, dream=boy_dreams[name])
