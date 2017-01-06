# -*- coding: utf-8 -*-

"""
Created on Wed Jan  4 09:26:44 2017

@author: 赵晓胜
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x_ave = np.zeros(101)
x_y0 = np.zeros(101)
#x_now = np.zeros(5000)
#x_now = np.zeros(1)
x_now = np.zeros(101)
for i in range(100):
#    for j in range(5000):
        ruler = np.random.rand()
        if ruler<=0.5:
#            x_now[j] = x_now[j] + 1
             x_now[i] = x_now[i] + 1
        else:
#            x_now[j] = x_now[j] - 1
             x_now[i] = x_now[i] - 1
#    average = sum(x_now)/5000
        sum1 = sum(x_now)
        x_ave[i+1] = sum1
#    x_ave[i+1] = average
    
#plt.scatter(steps, x_now)
#plt.scatter(steps, sum2)
plt.plot(steps, x_y0)
plt.scatter(steps, x_ave)
plt.xlim(0,100)
#plt.ylim(-1,1)
plt.ylim(-30,30)
plt.grid(True)
plt.xlabel('step number')
plt.ylabel('x')
#plt.title('<x> of 5000 walkers')
plt.title('Random walk in one dimension')
plt.show()