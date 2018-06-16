# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 21:11:30 2018

@author: Kamini

"""

from flask import Flask, render_template, request, url_for,json,jsonify
from Extraction import extract_data, classify_record
from UrlCheck import url_check
from Url_extend import url_mod
app = Flask(__name__)

#@app.route('/')
#@app.route('/index')
#def index():
#    return render_template('index.html')
   
@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def handle_req():
    if request.method=='POST':
        text=request.form['url']
        text=url_mod(text)
        if url_check(text):
            content=extract_data(text)
            result= classify_record(content)
            return jsonify({'output':result,'content':content })
        else:
            result="Oops!! Invalid URL...Please try again"
            return jsonify({'output':result, 'content':'none'})
            
    return render_template('index.html')
    
@app.route('/ajax_route',methods=['POST'])
def update_dataset():
    if request.method=='POST':
       print(request.json['content']+'\n\n\n'+request.json['class'])
             
    return render_template('index.html')
        
    
        
        
    

if __name__ == '__main__':
   app.run()