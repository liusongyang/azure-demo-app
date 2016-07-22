"""
Routes and views for the flask application.
"""

import os

from datetime import datetime
from flask import render_template, jsonify
from FlaskWebProject import app
from flask import request
from flask import json
from flask import panda as pd

points = [
    {
        'time': 1,
        'temp': 60,
        'done': False
    },
    {
        'id': 2,
        'temp': 50,
        'done': False
    }
]
@app.route('/')
@app.route('/home')
def home():
    return "Liusong is saying hello to you from NW hackathon!"

@app.route('/test')
def test():
    list = [
            {'a': 1, 'b': 2},
            {'a': 5, 'b': 10}
           ]
    return jsonify(results = list)

	
@app.route('/ml', methods=['POST'])
def doML():
    if not request.json or not 'temp' in request.json:
        abort(400)
    temp = {
        'id': points[-1]['id'] + 1,
        'temp': request.json['temp'],
        'done': True
    }
    points.append(temp)
    return jsonify({'temp': temp}), 201


