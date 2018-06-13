# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 21:11:30 2018

@author: Kamini

"""

from flask import Flask, render_template, request
from Extraction import extract_from_url
from UrlCheck import url_check

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
   return render_template('index.html')
   
   
@app.route('/',methods=['POST'])
@app.route('/index',methods=['POST'])
def handle_req():
    text = request.form['url']
    result = extract_from_url(text)
    return result
'''
def handle_req():
    if request.method=='POST':
        text=request.form['url']
        if url_check(text):
            result=extract_from_url(text)
            return json.dumps({'result':result})
        else:
            return json.dumps({'result':"Invalid url try again"})
'''

if __name__ == '__main__':
   app.run(debug=True)