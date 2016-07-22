"""
Routes and views for the flask application.
"""

import os

from datetime import datetime
from flask import render_template, jsonify
from FlaskWebProject import app
from flask import request
from flask import json
from flask import numpy as np

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

def mad_based_outlier(points, thresh=3.5):
    if len(points.shape) == 1:
        points = points[:,None]
    print points
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh

def percentile_based_outlier(data, threshold=95):
    diff = (100 - threshold) / 2.0
    minval, maxval = np.percentile(data, [diff, 100 - diff])
    return (data < minval) | (data > maxval)

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


