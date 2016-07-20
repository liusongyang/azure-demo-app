"""
Routes and views for the flask application.
"""

import os

from datetime import datetime
from flask import render_template
from FlaskWebProject import app


@app.route('/test')
def test():
    return "Hello, World!"

@app.route('/hello')
def hello():
    return  "my Hello, World!", 201
	
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

