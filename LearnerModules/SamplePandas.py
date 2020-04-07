# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:19:56 2020

@author: HOME
"""
import sklearn.
import matplotlib.pyplot as plt
import pandas as pd;
filePath="../../DataScience/DataSets/P14-Data-Preprocessing/Data_Preprocessing/data.csv"
df=pd.read_csv(filePath);
df
df.to_csv("data.csv", columns=["Age","Country"])
#converters in DataFrames
