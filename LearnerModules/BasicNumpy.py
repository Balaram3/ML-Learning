import numpy as np;
import pandas as pd;
from numpy import dtype

import matplotlib as plt
a=np.arange(1,21)
a=a.reshape(5,4)
print(a.reshape(20,))
df=pd.read_csv("../../DataScience/DataSets/P14-Data-Preprocessing/Data_Preprocessing/data.csv")
print(df)
print('\n')
print(df[['Country','Age']][df.Age>=30][df.Age<=40.0])