# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 21:11:30 2018

@author: Kamini

"""

from flask import Flask, render_template, request
from Extraction import extract_from_url
app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
   return render_template('index.html')
   
   
@app.route('/',methods=['POST'])
@app.route('/index',methods=['POST'])
def handle_req():
    text=request.form['url']
    result=extract_from_url(text)
    if result==True:
        return "YES"
    else:
        return "NO"
    

if __name__ == '__main__':
   app.run()