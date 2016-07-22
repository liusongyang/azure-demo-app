"""
Routes and views for the flask application.
"""

import os

from datetime import datetime
from flask import render_template, jsonify
from FlaskWebProject import app
from flask import request
import json
import pandas as pd

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
        item='{\"'+str(y.columns[0])+'\": ' +str(line[0])+', \"'+str(y.columns[1])+'\": '+ str(line[1])+', \"'+str(y.columns[2])+'\": '+str(line[2])+'}'
        #j.append(item)
        if i == 0:
            j=j+item
        else:
            j = j + ", " + item
                
    j=j+']'
    return j
	
@app.route('/ml', methods=['POST'])
def doML():
    inpt=u"[{\"flag\": \"False\", \"time\": 0,\"temp\":\"60\"},{\"flag\": \"False\", \"time\": 1,\"temp\":\"62\"}]"

    data_jason=json.loads(inpt)
 
    data=pd.DataFrame(data_jason)
   
    data_jason_flagged = df_to_json(data)
    
    return data_jason_flagged



