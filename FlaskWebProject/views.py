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
import numpy as np

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
    
    inpt=u"[{\"flag\": \"False\", \"time\": 0,\"temp\":\"60\"},{\"flag\": \"False\", \"time\": 1,\"temp\":\"62\"}]"
    
    #read data 
    data_jason=json.loads(inpt)
    #convert it to Jason
    data=pd.DataFrame(data_jason)
    
    one_column = data.iloc[:,1].apply(lambda x: float(x)) #Temparature col
    
    #outliers_perc = one_column[percentile_based_outlier(one_column)]
    outliers_MAD = one_column[mad_based_outlier(one_column)]
    
    #data.loc[:,"flag"] = None 
    data["flag"].iloc[outliers_MAD.index] = 1
    
    #convert data to Jason
    data_jason_flagged = df_to_json(data)
    
    #return jason file
    return data_jason_flagged
    
    

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
    j = '['
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

