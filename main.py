# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 21:11:30 2018

@author: Kamini

"""

from flask import Flask, render_template, request, url_for,json,jsonify
from Extraction import extract_from_url
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
            result=extract_from_url(text)
            return jsonify({'output':result})
        else:
            result="Oops!! Invalid URL...Please try again"
            return jsonify({'output':result})
            
    return render_template('index.html')
        
    
        
        
    

if __name__ == '__main__':
   app.run()