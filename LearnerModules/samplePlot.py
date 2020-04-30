# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,8)
y=[50,51,52,48,47,49,46]
plt.plot(x,y,'--d')
plt.plot(x,y,color="red",marker='D',linestyle='--')
%matplotlib inline
plt.grid()
##Bar Graph
company=['Facebook','Apple','Amazon','Netflix','Google']
revenue=[90,85,80,95,75]
profit=[5,6,7,2,4]
xpos=np.arange(len(company))
plt.xticks(xpos,company)
plt.barh(company,revenue,label='revenue')
plt.barh(company,profit,label='profit')
plt.legend()

##Histogram


