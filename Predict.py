# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 19:13:17 2018

@author: Kamini
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

def create_test_field(data):
    cv= CountVectorizer()
    Y=  cv.fit_transform(data).toarray()
    return Y
    