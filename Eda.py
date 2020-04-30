# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:31:52 2020

@author: HOME
"""
import numpy as np
import pandas as pd

path='./DataSets/airfoil_self_noise.csv'
dataset=pd.read_csv(path)
dataset.isna()
x_data=dataset.iloc[:,:-1]
y_data=dataset.iloc[:,-1]
from sklearn.models import train_test_split