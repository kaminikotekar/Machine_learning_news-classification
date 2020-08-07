# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 21:11:30 2018

@author: Kamini

"""
from flask import Flask, render_template, request, jsonify
from Extraction import extract_from_url
from UrlCheck import url_check
from Classification_model import predict_result

app = Flask(__name__)
main_url = 'http://127.0.0.1:5000/'
results_to_text = {0: 'News', 1: 'Sports', 2: 'Gadgets'}


@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html')
   

@app.errorhandler(404)
def page_not_found_404(e):
    return f"404 PAGE NOT FOUND<br><br>You will be redirected in 3 seconds</p><script>var timer = setTimeout(function() {{window.location='{main_url}'}}, 3000);</script></body></html>"


@app.errorhandler(Exception)
def page_not_found(e):
    return f"Something went Wrong <br> You will be redirected in 3 seconds</p><script>var timer = setTimeout(function() {{window.location='{main_url}'}}, 3000);</script></body></html>"


# @app.route('/', methods=['GET'])
# def handle_req():
#     print(request.form['url'])
#     text = request.form['url']
#     result = extract_from_url(text)
#     return result
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


@app.route('/api/text', methods=['GET'])
def api_id():
    text = request.args.get('txt', None)
    data = str(results_to_text.get(predict_result(text),"Error"))
    print(data)
    if text:
        return jsonify({'result': data})
    else:
        return 'Error'


if __name__ == '__main__':
   app.run(debug=False)