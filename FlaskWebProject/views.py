"""
Routes and views for the flask application.
"""

import os

from datetime import datetime
from flask import render_template, jsonify
from FlaskWebProject import app
from flask import request

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

def df_to_json(y):
    j = "["
    for i in xrange(len(y)):
        line=y.loc[i,:]
        #item={"flag": line[0],"time": line[1],"temp":line[2]}
        item='{\"'+str(col[0])+'\": ' +str(line[0])+', \"'+str(col[1])+'\": '+ str(line[1])+', \"'+str(col[2])+'\": '+str(line[2])+'}'
        #j.append(item)
        if i == 0:
            j=j+item
        else:
            j = j + ", " + item
                
    j=j+']'
    return j
	
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



