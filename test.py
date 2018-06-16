# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 16:55:01 2018

@author: Kamini
"""

import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df2 = pd.DataFrame([[3,4], [5,6]] ,columns=list('AB'))
df3=df.append(df, ignore_index= True)

dataset=pd.read_csv("News_dataset_csv.csv")

df=pd.DataFrame([["Portuguese talisman Cristiano Ronaldo scored his sixth hat trick for the national team and career treble as Portugal held an all-out attacking Spain in the Group clash at the Fisht Stadium in Sochi Russia on Saturday After the fivetime Ballon holder gave Portugal the initial lead Diego Costa scored the equaliser which was again cut to level by a goal each from the both Costa and Ronaldo for their respective sides second-half Nacho put Spain in the lead through a volley well curled into the far post from outside the box However a freekick given away to Portugal withing touching distance costed Spain the victory as the Portuguese captain brought back his national team on level terms ScorecardHighlights of 2018 FIFA World Cup match between Portugal and Spain straight from Fisht Stadium Sochi Russia","sports"]],columns=["content","class"])
with open('News_dataset_csv.csv', 'a') as f:
    df.to_csv(f, header=False)
dataset=pd.read_csv("News_dataset_csv.csv")

dataset.length
type(dataset)
len(dataset.index)