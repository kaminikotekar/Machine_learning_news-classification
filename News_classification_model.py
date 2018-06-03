# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:34:13 2018

@author: Kamini
"""

import pandas as pd
import numpy as np
import re
from nltk.stem import WordNetLemmatizer

#xlsl to csv
data_xls = pd.read_excel('News_dataset.xlsx', 'Sheet', index_col=None)
data_xls.to_csv('News_dataset_csv.csv', encoding='utf-8', index=False)

#natural language processing
corpus=[]
lemmatizer = WordNetLemmatizer()
dataset=pd.read_csv("News_dataset_csv.csv")
for i in range(20):
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
X=  cv.fit_transform(corpus).toarray()

#Target_label numpy array
target_label=[]
for i in range(20):
    if "news" in dataset['class'][i]:
        target_label.append(0)
    elif "sports" in dataset['class'][i]:
        target_label.append(1)
    elif "gadgets" in dataset['class'][i]:
        target_label.append(2)
        
Y = np.asarray(target_label)

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
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
accuracy= accuracy_score(y_test,y_pred)
