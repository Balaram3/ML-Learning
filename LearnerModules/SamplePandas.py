# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:19:56 2020

@author: HOME
"""
import pandas as pd;
filePath="../../DataScience/DataSets/P14-Data-Preprocessing/Data_Preprocessing/data.csv"
df=pd.read_csv(filePath);
df.to_csv("data.csv", columns=["Age","Country"])
#converters in DataFrames
#GroupBY in pandas
g=df.groupby('Country').mean()
g=df.groupby('Age').max()
g.describe()
df1=df[1:4]
df2=df[4:]
df_combined=pd.concat([df1,df2],ignore_index=True)
