# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 16:13:52 2018

@author: Kamini
"""

import requests,bs4,sys,nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import openpyxl
import os
import re
from nltk.stem import WordNetLemmatizer
from News_classification_model import predict, create_test_field


stop_words=set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
        
def extract_data(url):
    res=requests.get(url)
    if res.status_code == requests.codes.ok:
        soup=bs4.BeautifulSoup(res.text,'html.parser')
        content=soup.select("body")
        text = soup.get_text()
        text=re.sub(r'(<.*>)|(<.*/>)|({.*})'," ", text)
        filtered=re.sub('[^a-zA-Z]'," ",text)
        filtered= filtered.lower()
        filtered= filtered.split()
        new_filter=[]
        for word in filtered:
            if word not in stop_words:
                new_filter.append(lemmatizer.lemmatize(word))
        filtered=" ".join(new_filter)
        return filtered
        
def classify_record(content):
    print(content)
    llist=[]
    llist.append(content)
    X_data=create_test_field(llist)
    y_result=predict(X_data)
    if y_result[0]==0:
        print("news")
        return "news"
    elif y_result[0]==1:
        print("sports")
        return "sports"
    elif y_result[0]==2:
        print("gadgets")
        return "gadgets"
        
   
    
        

 
    
