# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:34:13 2018

@author: Kamini
"""

import pandas as pd
import numpy as np
import re
from nltk.stem import WordNetLemmatizer
import pickle

def make_classification():
    #xlsl to csv
    data_xls = pd.read_excel('News_dataset.xlsx', 'Sheet', index_col=None)
    data_xls.to_csv('News_dataset_csv.csv', encoding='utf-8', index=False)

    #natural language processing
    corpus=[]
    lemmatizer = WordNetLemmatizer()
    dataset=pd.read_csv("News_dataset_csv.csv")
    for i in range(30):
        filtered=re.sub('[^a-zA-Z]'," ",dataset['content'][i])
        filtered= filtered.lower()
        filtered= filtered.split()
        complete=[]
        for word in filtered:
            complete.append(lemmatizer.lemmatize(word))
        filtered=" ".join(complete)
        corpus.append(filtered)
        
    #Creatingthe bag of words model
    from sklearn.feature_extraction.text import CountVectorizer
    cv= CountVectorizer()
    cv.fit(corpus)
    X=cv.transform(corpus).toarray()

    #Target_label numpy array
    target_label=[]
    for i in range(30):
        if "news" in dataset['class'][i]:
            target_label.append(0)
        elif "sports" in dataset['class'][i]:
            target_label.append(1)
        elif "gadgets" in dataset['class'][i]:
            target_label.append(2)
            
    Y = np.asarray(target_label)

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.20, random_state = 0)

    # Fitting Naive Bayes to the Training set
    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)

    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)

    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(y_test,y_pred)

    return classifier, cv, cm, accuracy


def predict(X_data, classifier):
    y_result=classifier.predict(X_data)
    return y_result
    
    
def create_test_field(data, cv):
    X_test=cv.transform(data).toarray()
    return X_test


def save_model_data(classifier, cv):
    try:
        with open('data/model_data.pkl', 'wb') as f:
            pickle.dump(classifier, f)
        with open('data/cv_data.pkl', 'wb') as f:
            pickle.dump(cv, f)
        return True
    except Exception as e:
        print(e)
        return False
    # with open('data/filename.pkl', 'rb') as f:
    #     clf = pickle.load(f)

