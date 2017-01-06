# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 15:11:19 2017

@author: 赵晓胜
"""

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter 

def density(t_end):

    x = np.linspace(-50,50,101)
    y = np.linspace(-50,50,101)
    x,y = np.meshgrid(x,y)
    d = np.zeros((101,101))
    d[50][50]=1
    d1 = deepcopy(d)

    for t in range(t_end):
        for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    pass
                else:
                    d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])
        d1=deepcopy(d)

    for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    pass
                else:
                    if d[i][j]==0:
                        d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])

    return x,y,d

x,y,z = density(500)[0],density(500)[1],density(500)[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(x, y, z)
#surf =ax.plot_surface(x, y, z)
surf =ax.plot_surface(x, y, z,rstride=1, cstride=1, cmap=cm.jet,  
        linewidth=0, antialiased=False)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('density')
ax.set_title('Distribution in 2 dimensions(t=500)')
ax.zaxis.set_major_locator(LinearLocator(10))  
ax.zaxis.set_major_formatter(FormatStrFormatter('%.03f'))  
fig.colorbar(surf, shrink=0.5, aspect=7) 
plt.xlim(-50,50)
plt.ylim(-50,50)

plt.show()