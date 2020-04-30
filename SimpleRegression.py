# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:58:11 2020

@author: HOME
"""

import numpy as np
alpha=0.1
epsilon=1.e-6
#Data Generation

samples=100
x=np.linspace(0,1,samples)
y=15*x+5+np.random.normal(0,0.4,x.shape)

#Raw Data Visualization
import matplotlib.pyplot as plt
plt.scatter(x,y,marker='o')
w0=np.random.randint(1)
w1=np.random.randint(1)
j=[]
j.append((0.5/samples)*sum((y-w1*x-w0)**2))
error=1
i=0
dw0=0
dw1=0
while(error>0.001):
    yh=w1*x+w0
    dj0=yh-y
    dw0-=alpha*sum(dj0)/samples
    dj1=(yh-y)*x
    dw1-=alpha*sum(dj1)/samples
    w0+=dw0
    w1+=dw1
    i+=1
    j.append((0.5/samples)*sum((y-w1*x-w0)**2))
    error=abs(j[i]-j[i-1])
plt.scatter(x,y,marker='o')
plt.plot(x,yh,'r')
    
    